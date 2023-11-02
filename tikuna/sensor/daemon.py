import sys, os, time, atexit
from signal import SIGTERM

# A base and generic class for creating Linux deamons

class Daemon:

    def __init__(self, pidfile, stdin='/dev/null',
                 stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except (OSError) as e:
            sys.stderr.write("fork 1 failed: %d (%s)\n"
                             % (e.errno, e.strerror))
            sys.exit(1)
        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except (OSError) as e:
            sys.stderr.write("fork 2 failed: %d (%s)\n"
                             % (e.errno, e.strerror))
            sys.exit(1)
        sys.stdout.flush()
        sys.stderr.flush()
        with open(self.stdin, 'r') as si,\
             open(self.stdout, 'a+') as so,\
             open(self.stderr, 'a+') as se:
            os.dup2(si.fileno(), sys.stdin.fileno())
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())
        atexit.register(self.delpid)
        pid = str(os.getpid())
        with open(self.pidfile,'w+') as ou:
            ou.write("%s\n" % pid)

    def delpid(self):
        os.remove(self.pidfile)

    def start(self):
        try:
            with open(self.pidfile,'r') as pf:
                pid = int(pf.read().strip())
                pf.close()
        except IOError:
            pid = None

        if pid:
            message = ("pidfile %s already exist."
                      "Daemon already running?\n")
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        self.daemonize()
        self.run()

    def stop(self):
        try:
            with open(self.pidfile,'r') as pf:
                pid = int(pf.read().strip())
                pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return

        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except (OSError) as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        self.stop()
        self.start()

    def run(self):
        return None
