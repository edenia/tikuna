import sys, time
import logging
import socket

from daemon import Daemon
from queue import Queue, Empty
from tikuna.sensor.log_sensor import LogSensor

# The tikuna daemon service that collects security
# monitoring information.

# TODO: this should be configured by files
data_path = "/var/lib/tikuna/data"
log_path  = "/var/log/tikuna/"
log_file  = "%s/%s-tikuna-sensor.log" % (log_path, socket.gethostname())
pid_file  = "/var/lib/tikuna/tikuna-sensor.pid"

class SensorDaemon(Daemon):

    def run(self):
        logging.basicConfig(filename=log_file,
                            level=logging.INFO)
        logging.info('Creating tikuna client services...')
        log_sensor_service = tikunaSensors(None)
        # Start the services.
        logging.info('Starting the tikuna client services...')
        log_sensor_service.start_sensors()
        logging.info('tikuna service client started...')

    def stop(self):
        # TODO: do something here?
        logging.info('Service tikuna stopped ...')

if __name__ == "__main__":
    daemon = SensorDaemon( pid_file,
                            stdout=log_file,
                            stderr=log_file)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)