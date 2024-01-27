import sys, time
import logging
import socket

from daemon import Daemon
from queue import Queue, Empty
from log_sensor import LogSensor

# The tikuna daemon service that collects security
# monitoring information.

# TODO: this should be configured by files
data_path = "/var/lib/tikuna/data"
log_path  = "/var/log/tikuna/"
log_file  = "%s/%s-tikuna-sensor.log" % (log_path, socket.gethostname())
pid_file  = "/var/lib/tikuna/tikuna-sensor.pid"

class SensorDaemon(Daemon):

    def __init__(self, pidfile, stdin='/dev/null',
                 stdout='/dev/null', stderr='/dev/null'):
        super(Daemon, self).__init__()
        self.pidfile = pidfile
        self.stdin = stdin
        self.stdout = log_file
        self.stderr = log_file
        self.log_sensor_service = None

    def run(self):
        logging.basicConfig(filename=log_file,
                            level=logging.INFO)
        logging.info('Creating Tikuna client service...')
        self.log_sensor_service = LogSensor("prysm-beacon")
        # Start the services.
        logging.info('Starting the Tikuna client service...')
        self.log_sensor_service.start()
        logging.info('Tikuna service client started...')

if __name__ == "__main__":
    daemon = SensorDaemon( pid_file,
                            stdout=log_file,
                            stderr=log_file)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            logging.info('Starting Tikuna sensor service...')
            daemon.start()
        elif 'stop' == sys.argv[1]:
            logging.info('Stoping Tikuna sensor service...')
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            logging.info('Restarting Tikuna sensor service...')
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)
