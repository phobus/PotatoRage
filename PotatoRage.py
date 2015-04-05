#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import sys
import logging

from lib.daemon import Daemon

__author__ = 'Pablo Alvao'
__version__ = '0.1'
__license__ = ''
                
class PRDaemon(Daemon):
    def __init__(self, daemon, pidfile, datadir, config, port, host,
                 start, stop, restart, status):
        self.host = host
        self.port = port
        # home full dir
        myFullName = os.path.normpath(os.path.abspath(__file__))
        home_dir = os.path.dirname(myFullName)
        
        self.data_dir = datadir;
        # check data directory
        if not self.data_dir:
            self.data_dir = os.path.join(home_dir, 'data')
        
        
        # If they don't specify a config file then put it in the data dir
        if not config:
            config = os.path.join(self.data_dir, 'config.ini')
            
        # log 
        logfile = os.path.join(self.data_dir, 'potatorage.log')
        
        # Make sure that we can create the data dir
        if not os.access(self.data_dir, os.F_OK):
            try:
                os.makedirs(self.data_dir, 0744)
            except os.error, e:
                raise SystemExit("Unable to create datadir '" + self.data_dir + "'")
        
        # Make sure we can write to the data dir
        if not os.access(self.data_dir, os.W_OK):
            raise SystemExit("Datadir must be writeable '" + self.data_dir + "'")

        # Make sure we can write to the config file
        if not os.access(config, os.W_OK):
            if os.path.isfile(config):
                raise SystemExit("Config file '" + config + "' must be writeable.")
            elif not os.access(os.path.dirname(config), os.W_OK):
                raise SystemExit(
                    "Config file root dir '" + os.path.dirname(config) + "' must be writeable.")
        
        # Make sure we can write to the log file
        if not os.access(logfile, os.W_OK):
            if os.path.isfile(config):
                raise SystemExit("Log file '" + logfile + "' must be writeable.")
            elif not os.access(os.path.dirname(logfile), os.W_OK):
                raise SystemExit(
                    "Log file root dir '" + os.path.dirname(logfile) + "' must be writeable.")
                
        # The pidFile is only useful in daemon mode, make sure we can write the file properly
        if daemon and pidfile != None:
            pid_dir = os.path.dirname(pidfile)
            if not os.access(pid_dir, os.F_OK):
                sys.exit("PID dir: " + pid_dir + " doesn't exist. Exiting.")
            if not os.access(pid_dir, os.W_OK):
                sys.exit("PID dir: " + pid_dir + " must be writable (write permissions). Exiting.")

        else:
            sys.stdout.write("Not running in daemon mode. PID file creation disabled.\n")

        self.createLog(logfile)
        
        Daemon.__init__(self,
                        pidfile,
                        stdin=logfile,
                        stdout=logfile,
                        stderr=logfile,
                        home_dir=home_dir)
        
    def createLog(self, logfile):
        self.logger = logging.getLogger('potatorage')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.DEBUG)
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        
    def run(self):
        from potatorage.app import PotatoRage
        PotatoRage(self.home_dir, self.data_dir, self.host, self.port)
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Star daemon and webserver for PotatoRage %s the Torrent manager' % __version__)
    
    parser.add_argument('--daemon', action='store_true', help='run as daemon')
    parser.add_argument('--pidfile', help='Combined with --daemon creates a pidfile (full path including filename)')
    
    parser.add_argument('--datadir', help='full path data folder')
    parser.add_argument('--config', help='full path to the file')
    
    parser.add_argument('--port', type=int, default=8080, help='port to listen default 8080')
    parser.add_argument('--host', default='0.0.0.0', help='host default 0.0.0.0')
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--start', action='store_true')
    group.add_argument('--stop', action='store_true')
    group.add_argument('--restart', action='store_true')
    group.add_argument('--status', action='store_true')
    
    args = parser.parse_args()
    
    daemon = PRDaemon(**vars(args))
    if args.start:
        daemon.start()
    elif args.stop:
        daemon.stop()
    elif args.restart:
        daemon.restart()
    elif args.status:
        daemon.is_running()
    else:
        daemon.run()