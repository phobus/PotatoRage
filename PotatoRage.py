#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import sys
import signal

import logging

from lib.daemon import Daemon

from potatorage import setup

__author__ = 'Pablo Alvao'
__version__ = '0.0.16'
__license__ = 'free'
                
class PRDaemon(Daemon):
    def __init__(self, daemon, pidfile, datadir, config, host, port,
                 start, stop, restart, status):
        setup.HOST = host
        setup.PORT = port
        
        # home full dir
        myFullName = os.path.normpath(os.path.abspath(__file__))
        setup.HOME_DIR = os.path.dirname(myFullName)
        
        # check data directory
        if not datadir:
            datadir = os.path.join(setup.HOME_DIR, 'data')
        self.checkFolder(datadir)
        setup.DATA_DIR = datadir;
        
        # If they don't specify a config file then put it in the data dir
        if not config:
            config = os.path.join(setup.DATA_DIR, 'config.ini')
        self.checkFile(config)
           
        # log 
        logfile = os.path.join(setup.DATA_DIR, 'potatorage.log')
        self.checkFile(logfile)        
        self.createLog(logfile)
              
        # The pidFile is only useful in daemon mode, make sure we can write the file properly
        if daemon and pidfile != None:
            self.checkFile(pidfile)
        else:
            sys.stdout.write("Not running in daemon mode. PID file creation disabled.\n")

        Daemon.__init__(self,
                        pidfile,
                        stdin=logfile,
                        stdout=logfile,
                        stderr=logfile,
                        home_dir=setup.HOME_DIR)
        
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
        
    def checkFile(self, filepath):
        if not os.access(filepath, os.W_OK):
            if os.path.isfile(filepath):
                raise SystemExit("File '%s' must be writable." % os.path.dirname(logfile))
            elif not os.access(os.path.dirname(filepath), os.W_OK):
                raise SystemExit("Folder '%s' must be writable." % os.path.dirname(logfile))
    
    def checkFolder(self, folderpath):
        if not os.access(folderpath, os.F_OK):
            try:
                os.makedirs(folderpath, 0744)
            except os.error, e:
                raise SystemExit("Unable to create '%s'" % folderpath)
        
        if not os.access(folderpath, os.W_OK):
            raise SystemExit("Folder '%s' must be writable " % folderpath)
    
    def sigtermhandler(self, signum, frame):
        self.daemon_alive = False
        
    def run(self):
        signal.signal(signal.SIGTERM, self.sigtermhandler)
        signal.signal(signal.SIGINT, self.sigtermhandler)
        
        from potatorage import webserver
        webserver.run()
        
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Star daemon and web server for PotatoRage %s the Torrent manager' % __version__)
    
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
