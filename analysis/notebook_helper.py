import os
import json
import pathlib
import multiprocessing as mp
from glob import glob
import pandas as pd
import toml
import ipywidgets as widgets
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import zipfile
import subprocess
import base58
import base64
import sys
from collections import defaultdict
from functools import reduce
# import pandas_sets # imported for side effects, don't remove!


# tracer event types
TYPE_GRAFT = 11
TYPE_PRUNE = 12


def mkdirp(dirpath):
    pathlib.Path(dirpath).mkdir(parents=True, exist_ok=True)

# sugar around recursive glob search
def find_files(dirname, filename_glob):
    path = '{}/**/{}'.format(dirname, filename_glob)
    return glob(path, recursive=True)

def empty_scores_dataframe():
    return pd.DataFrame([], columns=['observer', 'peer', 'timestamp', 'score']).astype(
        {'score': 'float64', 'observer': 'int64', 'peer': 'int64', 'timestamp': 'datetime64[ns]'})

def load_trace_data(traces_filepath):
    # load trace data
    print('Loading test data from ' + traces_filepath)
    if not os.path.exists(traces_filepath+"/pandas/traces.gz"):
        cols = ['type', 'peerID', 'timestamp']
        data = []

        with open(traces_filepath+"/full-trace.json") as f:
            for line in f:
                doc = json.loads(line)
                lst = [doc['type'], doc['peerID'], doc['timestamp']]
                data.append(lst)

        traces = pd.DataFrame(data=data, columns=cols)
        traces.to_pickle(traces_filepath+"/pandas/traces.gz")
    else:
        traces = pd.read_pickle(traces_filepath+"/pandas/traces.gz")
    peer_info_filename = os.path.join(traces_filepath, 'peer-info.json')
    peers = peer_info_to_pandas(peer_info_filename)
    # select the cols from peers table we want to join on
    p = peers[['peer_id', 'seq', 'honest']]
    peers = traces.peerID.unique()
    traces['timestamp'] = pd.to_datetime(traces['timestamp'])
    traces.set_index('timestamp', inplace=True)
    traces = traces.groupby(['peerID', pd.Grouper(freq='0.1S')])['type'].value_counts()
    traces = traces.unstack(level="type", fill_value=0)\
    .reset_index(level=["peerID", "timestamp"])
    traces.rename(columns = {'peerID':'peer_id'}, inplace = True)
    traces['peer_id'] = traces['peer_id'].apply(lambda x: b64_to_b58(x))
    traces = traces.merge(p, on='peer_id')
    traces = traces.drop(columns=['peer_id'])
    traces = traces.rename(columns={'seq': 'peer'})
    traces = traces.sort_values(['peer', 'timestamp'])
    return traces

def aggregate_peer_scores_single(scores_filepath, peers_table):
    df = empty_scores_dataframe()

    # select the cols from peers table we want to join on
    p = peers_table[['peer_id', 'seq', 'honest']]

    with open(scores_filepath, 'rt') as f:
        for line in iter(f.readline, ''):
            try:
                data = json.loads(line)
            except BaseException as err:
                print('error parsing score json: ', err)
                continue
            scores = pd.json_normalize(data['Scores'], max_level=0)
            scores = scores.T \
                .rename(columns={0: 'score'}) \
                .reset_index() \
                .rename(columns={'index': 'peer_id'})
            score_json = pd.json_normalize(scores['score'], max_level=0)
            scores = pd.concat([scores, score_json], axis=1)
            scores = scores.drop('score', axis=1)
            scores = scores.rename(columns={'Score': 'score'})
            scores['timestamp'] = pd.to_datetime(data['Timestamp'])
            scores['observer_id'] = data['PeerID']

            # join with peers table to convert peer ids to seq numbers
            s = scores.merge(p, on='peer_id').drop(columns=['peer_id'])
            s = s.merge(p.drop(columns=['honest']), left_on='observer_id', right_on='peer_id', suffixes=['_peer', '_observer'])
            s = s.drop(columns=['peer_id', 'observer_id'])
            s = s.rename(columns={'seq_peer': 'peer', 'seq_observer': 'observer'})

            df = df.append(s, ignore_index=True)
    topics = pd.json_normalize(df['Topics']).copy()
    topics.reset_index(drop=True, inplace=True)
    df = df.drop('Topics', axis=1)
    df = pd.concat([df, topics], axis=1)
    df.set_index('timestamp', inplace=True)
    return df


def aggregate_peer_scores(score_filepaths, peers_table):
    if len(score_filepaths) == 0:
        return empty_scores_dataframe()
    pool = mp.Pool(mp.cpu_count())
    args = [(f, peers_table) for f in score_filepaths]
    results = pool.starmap(aggregate_peer_scores_single, args)
    # concat all data frames into one
    return pd.concat(results)


def empty_metrics_dataframe():
    return pd.DataFrame([], columns=['published', 'rejected', 'delivered', 'duplicates', 'droppedrpc',
                                     'peersadded', 'peersremoved', 'topicsjoined', 'topicsleft', 'peer',
                                     'sent_rpcs', 'sent_messages', 'sent_grafts', 'sent_prunes',
                                     'sent_iwants', 'sent_ihaves', 'recv_rpcs', 'recv_messages',
                                     'recv_grafts', 'recv_prunes', 'recv_iwants', 'recv_ihaves'])


def aggregate_metrics_to_pandas_single(metrics_filepath, peers_table):
    def munge_keys(d, prefix=''):
        out = dict()
        for k, v in d.items():
            outkey = prefix + k.lower()
            out[outkey] = v
        return out


    rows = list()
    with open(metrics_filepath, 'rb') as f:
        try:
            e = json.load(f)
        except BaseException as err:
            print('error loading metrics entry: ', err)
        else:
            pid = e['LocalPeer']
            sent = munge_keys(e['SentRPC'], 'sent_')
            recv = munge_keys(e['ReceivedRPC'], 'recv_')
            del(e['LocalPeer'], e['SentRPC'], e['ReceivedRPC'])
            row = munge_keys(e)
            row.update(sent)
            row.update(recv)
            rows.append(row)
            row['peer_id'] = pid

    df = pd.DataFrame(rows)
    p = peers_table[['peer_id', 'seq']]
    df = df.merge(p, on='peer_id').drop(columns=['peer_id']).rename(columns={'seq': 'peer'})
    return df.astype('int64')


def aggregate_metrics_to_pandas(metrics_filepaths, peers_table):
    if len(metrics_filepaths) == 0:
        return empty_metrics_dataframe()
    pool = mp.Pool(mp.cpu_count())
    args = [(f, peers_table) for f in metrics_filepaths]
    results = pool.starmap(aggregate_metrics_to_pandas_single, args)
    # concat all data frames into one
    return pd.concat(results)


def cdf_to_pandas(cdf_filepath):
    if os.path.exists(cdf_filepath):
        return pd.read_csv(cdf_filepath, delim_whitespace=True, names=['delay_ms', 'count'], dtype='int64')
    else:
        return pd.DataFrame([], columns=['delay_ms', 'count'], dtype='int64')


def peer_info_to_pandas(peer_info_filename):
    with open(peer_info_filename, 'rt') as f:
        data = json.load(f)
    peers = pd.json_normalize(data)
    peers['honest'] = peers['type'] == 'honest'
    return peers.astype({'type': 'category',
                         't_warm': 'datetime64[ns]',
                         't_connect': 'datetime64[ns]',
                         't_run': 'datetime64[ns]',
                         't_cool': 'datetime64[ns]',
                         't_complete': 'datetime64[ns]'})



def trace_event_stream(trace_filename):
    """
    Convert the trace events in trace_filename to python dicts (via json)
    :param trace_filename: gzipped file of protobuf trace events
    :return: a generator that yields a dictionary representation of each event.
    """
    cmd = ['go', 'run', 'github.com/libp2p/go-libp2p-pubsub-tracer/cmd/trace2json', trace_filename]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for line in p.stdout:
        yield json.loads(line)


def mesh_trace_event_stream(trace_filename):
    """
    Converts the trace events in trace_filename to python dicts, filtering out
    everything except GRAFT / PRUNE events.
    :param trace_filename: gzipped file of protobuf trace events
    :return: a generator that yields a dictionary representation of each event.
    """
    for event in trace_event_stream(trace_filename):
        typ = event.get('type', -1)
        if typ == TYPE_GRAFT or typ == TYPE_PRUNE:
            yield event


def mesh_events_to_pandas(event_stream, peers_table, sample_freq='5s'):
    """
    Converts a stream of GRAFT / PRUNE tracer events to a pandas dataframe
    containing the state of each peers mesh, sampled at sample_freq intervals.
    """

    def empty_mesh_events_table():
        return pd.DataFrame([], columns=['timestamp', 'peer', 'grafted', 'pruned']).astype({
            'timestamp': 'datetime64[ns]',
            'peer': 'int64',
        }).set_index('timestamp')

    # building the mesh state is simpler if we have one DataFrame per peer
    # and concat them together at the end.
    tables = defaultdict(empty_mesh_events_table)

    # first we build up a table of grafts / prunes. The 'grafted' and 'pruned' columns
    # contain python set objects with the seq id of the grafted or pruned peer.
    # These sets are used below to derive the mesh state.
    last_timestamp = pd.to_datetime(0)
    for evt in event_stream:
        typ = evt.get('type', -1)
        if typ == TYPE_GRAFT:
            info = evt['graft']
        elif typ == TYPE_PRUNE:
            info = evt['prune']
        else:
            print('unexpected event type {}'.format(typ), file=sys.stderr)
            continue

        timestamp = pd.to_datetime(evt['timestamp'])
        if timestamp > last_timestamp:
            last_timestamp = timestamp
        topic = info['topic']  # TODO: multiple topics
        peer = numeric_peer_id(b64_to_b58(evt['peerID']), peers_table)
        remote_peer = numeric_peer_id(b64_to_b58(info['peerID']), peers_table)

        df = tables[peer]

        grafted = set()
        pruned = set()
        if typ == TYPE_GRAFT:
            grafted.add(remote_peer)
        if typ == TYPE_PRUNE:
            pruned.add(remote_peer)
        row = [peer, grafted, pruned]
        df.loc[timestamp] = row

    # reducer to return the union of all sets in a column, used when resampling
    def set_union(series):
        return reduce(lambda x, y: x.union(y), series, set())

    resampled = []
    for peer, table in tables.items():
        # we add an empty row at last_timestamp to each table, so that all the
        # tables cover the same time span before resampling
        table.loc[last_timestamp] = [peer, set(), set()]

        # resample the raw grafts / prunes into windows of 5 secs (by default)
        # the 'grafted' and 'pruned' columns for each window will contain the
        # union of all peers grafted or pruned within the window
        t = table[['grafted', 'pruned']].resample(sample_freq).agg(set_union)

        # we collect the mesh state here by iterating over the resampled table applying the grafts and prunes
        mesh = set()

        # series objects to contain the mesh state, plus the number of honest / dishonest peers
        # in the mesh for a given time window
        meshes = pd.Series(index=t.index, dtype='object')
        honest = pd.Series(index=t.index, dtype='int16')
        attacker = pd.Series(index=t.index, dtype='int16')
        for index, row in t.iterrows():
            mesh.update(row['grafted'])
            mesh.difference_update(row['pruned'])
            meshes[index] = mesh.copy()
            h, a = classify_mesh_peers(mesh, peers_table)
            honest[index] = len(h)
            attacker[index] = len(a)
        # add the new columns and drop the raw grafted / pruned cols
        t['mesh'] = meshes
        t['n_mesh_honest'] = honest
        t['n_mesh_attacker'] = attacker
        t['peer'] = peer
        resampled.append(t.drop(columns=['grafted', 'pruned']))

    df = pd.concat(resampled)
    # TODO: make multiindex of [timestamp, peer]
    return df


def empty_meshes_table(sample_freq='5s'):
    index = pd.date_range(0, periods=0, freq=sample_freq)
    return pd.DataFrame(index=index, columns=['mesh', 'n_mesh_honest', 'n_mesh_attacker', 'peer'])


def b64_to_b58(b64_str):
    b = base64.b64decode(b64_str)
    return base58.b58encode(b).decode('utf8')


def numeric_peer_id(pid_str, peers_table):
    """
    Given a base58 peer id string and a table of peer info, returns the numeric seq number
    for the peer.
    """
    try:
        pid = peers_table[['peer_id', 'seq']].where(peers_table['peer_id'] == pid_str).dropna()['seq'].iloc[0]
        return int(pid)
    except BaseException as err:
        print('unable to get numeric id for peer {}: {}'.format(pid_str, err), file=sys.stderr)
        return -1


def classify_mesh_peers(mesh, peers_table):
    """
    Given a set of peer seq numbers and a table of peer info, returns two sets.
    The first contains honest peers, the second dishonest peers.
    """
    peers = peers_table.set_index('seq')
    mesh_honest = set()
    mesh_attacker = set()
    for p in mesh:
        try:
            honest = peers.loc[p]['honest']
        except KeyError:
            continue
        if honest:
            mesh_honest.add(p)
        else:
            mesh_attacker.add(p)
    return mesh_honest, mesh_attacker


def do_mesh_to_pandas(aggregate_output_dir, pandas_output_dir, peers_table, sample_freq='5s'):
    print('deriving mesh state & converting to pandas...')
    trace_file = os.path.join(aggregate_output_dir, 'filtered-trace.bin.gz')
    df = mesh_events_to_pandas(mesh_trace_event_stream(trace_file), peers_table, sample_freq=sample_freq)
    outfile = os.path.join(pandas_output_dir, 'meshes.gz')
    print('writing mesh states to {}'.format(outfile))
    df.to_pickle(outfile)
    return df


def to_pandas(aggregate_output_dir, pandas_output_dir, include_mesh=False):
    mkdirp(pandas_output_dir)

    print('converting peer ids and info to pandas...')
    peer_info_filename = os.path.join(aggregate_output_dir, 'peer-info.json')
    peers = peer_info_to_pandas(peer_info_filename)
    outfile = os.path.join(pandas_output_dir, 'peers.gz')
    peers.to_pickle(outfile)

    print('converting peer scores to pandas...')
    scores_files = find_files(aggregate_output_dir, 'peer-scores*')
    df = aggregate_peer_scores(scores_files, peers)
    outfile = os.path.join(pandas_output_dir, 'scores.gz')
    print('writing pandas peer scores to {}'.format(outfile))
    df.to_pickle(outfile)

    if include_mesh:
        do_mesh_to_pandas(aggregate_output_dir, pandas_output_dir, peers)

    print('converting aggregate metrics to pandas...')
    outfile = os.path.join(pandas_output_dir, 'metrics.gz')
    metrics_files = find_files(aggregate_output_dir, '*aggregate.json')
    df = aggregate_metrics_to_pandas(metrics_files, peers)
    print('writing aggregate metrics pandas data to {}'.format(outfile))
    df.to_pickle(outfile)

    print('converting latency cdf to pandas...')
    outfile = os.path.join(pandas_output_dir, 'cdf.gz')
    cdf_file = os.path.join(aggregate_output_dir, 'tracestat-cdf.txt')
    df = cdf_to_pandas(cdf_file)
    print('writing cdf pandas data to {}'.format(outfile))
    df.to_pickle(outfile)


def load_pandas(analysis_dir, derive_meshes_if_missing=False, mesh_sample_freq='5s'):
    analysis_dir = os.path.abspath(analysis_dir)
    pandas_dir = os.path.join(analysis_dir, 'pandas')
    raw_data_dir = os.path.join(analysis_dir, 'raw-data')

    # if the raw-data dir doesn't exist, assume that we're running against an
    # output directory that was extracted with an earlier version, which put
    # the raw data in the "analysis" dir
    if not os.path.exists(raw_data_dir):
        raw_data_dir = analysis_dir

    if not os.path.exists(pandas_dir):
        print('Cached pandas data not found. Converting analysis data from {} to pandas'.format(raw_data_dir))
        to_pandas(raw_data_dir, pandas_dir)

    tables = {}
    for f in os.listdir(pandas_dir):
        if not f.endswith('.gz'):
            continue
        name = os.path.splitext(f)[0]
        tables[name] = pd.read_pickle(os.path.join(pandas_dir, f))

    if 'cdf' in tables:
        tables['pdf'] = cdf_to_pdf(tables['cdf'])

    if derive_meshes_if_missing and not os.path.exists(os.path.join(pandas_dir, 'meshes.gz')):
        peers_table = tables['peers']
        print('Mesh data not found, and derive_meshes_if_missing==True, deriving meshes')
        tables['meshes'] = do_mesh_to_pandas(raw_data_dir, pandas_dir, peers_table, sample_freq=mesh_sample_freq)

    return tables


def test_params_panel(analysis_dir):
    param_filename = os.path.join(analysis_dir, '..', 'template-params.toml')
    with open(param_filename, 'rt') as f:
        contents = f.read()
        test_params = toml.loads(contents)

    params_out = widgets.Output()
    with params_out:
        print(contents)

    params_panel = widgets.Accordion([params_out])
    params_panel.set_title(0, 'Test Parameters')
    params_panel.selected_index = None
    return (params_panel, test_params)


def save_fig_fn(dest, formats=['png', 'pdf']):
    mkdirp(dest)

    def save_fig(fig, filename, **kwargs):
        try:
            for fmt in formats:
                base = os.path.splitext(filename)[0]
                name = os.path.join(dest, '{}.{}'.format(base, fmt))
                fig.savefig(name, format=fmt, **kwargs)
        except BaseException as err:
            print('Error saving figure to {}: {}'.format(filename, err))
    return save_fig


def zipdir(path, ziph, extensions=['.png', '.pdf', '.eps', '.svg']):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            strs = os.path.splitext(file)
            if len(strs) < 2:
                continue
            ext = strs[1]
            if ext not in extensions:
                continue
            ziph.write(os.path.join(root, file))


def archive_figures(figure_dir, out_filename):
    zipf = zipfile.ZipFile(out_filename, 'w', zipfile.ZIP_DEFLATED)
    zipdir(figure_dir, zipf)
    zipf.close()


def no_scores_message():
    from IPython.display import display, Markdown
    display(Markdown("""##### No peer score data, chart omitted"""))


def no_meshes_message():
    from IPython.display import display, Markdown
    display(Markdown("""##### No mesh data, chart omitted. To generate mesh data, re-run with `DERIVE_MESHES=True`"""))


def tracestat_summary(analysis_dir):
    summary_file = os.path.join(analysis_dir, 'tracestat-summary.txt')
    if os.path.exists(summary_file):
        with open(summary_file, 'rt') as f:
            return f.read()
    else:
        return('no tracestat summary file found')


def make_line(label, ax, x, color, alpha=0.5, linestyle='dashed'):
    ax.axvline(x=x, linestyle=linestyle, color=color, alpha=alpha)
    return mlines.Line2D([], [], color=color, linestyle=linestyle, label=label, alpha=alpha)


def make_span(label, ax, start, end, color, alpha=0.3):
    ax.axvspan(start, end, facecolor=color, alpha=alpha)
    return mpatches.Patch(color=color, alpha=alpha, label=label)


def annotate_times(ax, time_annotations, legend_anchor=None):
    colors = sns.color_palette('Set2')
    def next_color():
        c = colors.pop(0)
        colors.append(c)
        return c

    legends = []
    for a in time_annotations:
        t1 = a['time']
        if pd.isnull(t1):
            continue
        label = a['label']
        if 'end_time' in a:
            # if we have an end_time, draw a span between start and end
            t2 = a['end_time']
            if pd.isnull(t2):
                continue
            legends.append(make_span(label, ax, t1, t2, next_color()))
        else:
            # otherwise, draw a dashed line at t1
            legends.append(make_line(label, ax, t1, next_color()))

    if len(legends) != 0 and legend_anchor is not None:
        # add the original legend to the plot
        ax.add_artist(ax.legend(loc='upper left'))
        # add second legend for marker lines
        ax.legend(handles=legends, bbox_to_anchor=legend_anchor, loc='upper left')


def annotate_score_plot(plot, title, legend_anchor=None, time_annotations=[]):
    plot.set_title(title)
    plot.set_ylabel('score')
    plot.set_xlabel('')
    if len(time_annotations) != 0:
        annotate_times(plot, time_annotations, legend_anchor=legend_anchor)


def draw_latency_threshold_lines(max_val, eth_threshold=3000, fil_threshold=6000):
    legends = []
    if max_val > eth_threshold * 0.75:
        plt.axvline(eth_threshold, linestyle='--', color='orange')
        l = mlines.Line2D([], [], color='orange', linestyle='--', label='Eth2 threshold')
        legends.append(l)

    if max_val > fil_threshold * 0.75:
        plt.axvline(fil_threshold, linestyle='--', color='blue')
        l = mlines.Line2D([], [], color='blue', linestyle='--', label='Fil threshold')
        legends.append(l)

    if len(legends) > 0:
        plt.legend(handles=legends)


def plot_latency_cdf(cdf):
    fig = plt.figure(figsize=(11,6))
    fig.suptitle("Latency CDF")
    plt.plot('delay_ms', 'count', data=cdf)
    plt.ylabel('messages')
    plt.xlabel('ms to fully propagate')
    draw_latency_threshold_lines(cdf['delay_ms'].max())
    plt.show()
    return fig


def plot_latency_pdf(pdf):
    fig = plt.figure(figsize=(11,6))
    fig.suptitle('Latency Distribution (PDF)')
    plt.hist(pdf['delay_ms'], weights=pdf['count'], bins=50)
    plt.ylabel('messages')
    plt.xlabel('ms to fully propagate')
    draw_latency_threshold_lines(pdf['delay_ms'].max())
    plt.show()
    return fig


def plot_latency_pdf_above_quantile(pdf, quantile=0.99):
    delays = pdf.reindex(pdf.index.repeat(pdf['count']))
    q = delays['delay_ms'].quantile(quantile)

    fig = plt.figure(figsize=(11,6))
    qname = 'p{}'.format(int(round(quantile, 2) * 100))
    fig.suptitle('Latency PDF above {} ({:.2f}ms)'.format(qname, round(q, 2)))
    delays['delay_ms'].where(delays['delay_ms'] > q).dropna().plot.hist(bins=50)
    plt.ylabel('messages')
    plt.xlabel('ms to fully propagate')
    plt.show()
    return fig


def cdf_to_pdf(cdf):
    delta = [0] * len(cdf['count'])
    delta[0] = cdf['count'][0]
    for x in range(1, len(cdf['count'])):
        delta[x] = cdf['count'][x] - cdf['count'][x-1]
    return pd.DataFrame({'delay_ms': cdf['delay_ms'], 'count': delta})


def p25(x):
    return np.percentile(x, q=25)


def p50(x):
    return np.percentile(x, q=50)


def p75(x):
    return np.percentile(x, q=75)


def p95(x):
    return np.percentile(x, q=95)


def p99(x):
    return np.percentile(x, q=99)
