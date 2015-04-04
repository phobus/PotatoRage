#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import sys
import os
import signal
import logging

import getopt

from potatorage.potatorage import PotatoRage
 
class Loader:
    def __init__(self):
        self.configFile = None
        self.dataDir = None
        self.progDir = None
        
        self.runAsDaemon = False
        self.createPid = False
        self.pidFile = None
        self.daemon = None
        

        self.webPort = '8080'

        self.loadParam()
        self.setup()
        
        self.logFile = os.path.join(self.dataDir, 'potatorage.log')
        # create logger'
        self.logger = logging.getLogger('potatorage')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(self.logFile)
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
        
        self.logger.info("initPid %s" % os.getpid())
        self.logger.info("runAsDaemon %s" % self.runAsDaemon)
        self.logger.info("pidFile %s" % self.pidFile)       
        
    def helpMessage(self):
        return "Usage: TO DO"
            
    def loadParam(self): 
        myFullName = os.path.normpath(os.path.abspath(__file__))
        
        self.progDir = os.path.dirname(myFullName)
        self.dataDir = os.path.join(self.progDir, 'data')
        
        try:
            opts, args = getopt.getopt(# args
                                       sys.argv[1:],
                                       # options
                                       "hdp::",
                                       # long_options
                                       ['help', 'daemon', 'port=',
                                        'pidfile=', 'datadir=', 'config='])
        except getopt.GetoptError:
            sys.exit(self.helpMessage())
            
        for o, a in opts:
            # Prints help message
            if o in ('-h', '--help'):
                sys.exit(self.help_message())

            # Run as a double forked daemon
            if o in ('-d', '--daemon'):
                self.runAsDaemon = True
                
            # Override default/configured port
            if o in ('-p', '--port'):
                try:
                    self.WebPort = int(a)
                except ValueError:
                    sys.exit("Port: " + str(a) + " is not a number. Exiting.")

            # Write a pidfile if requested
            if o in ('--pidfile',):
                self.createPid = True
                self.pidFile = str(a)

                # If the pidFile already exists, sickbeard may still be running, so exit
                if os.path.exists(self.pidFile):
                    sys.exit("PID file: " + self.pidFile + " already exists. Exiting.")

            # Specify folder to use as the data dir
            if o in ('--datadir',):
                self.dataDir = os.path.abspath(a)
                
            # Specify folder to load the config file from
            if o in ('--config',):
                self.configFile = os.path.abspath(a)
    
    def setup(self):   
        # If they don't specify a config file then put it in the data dir
        if not self.configFile:
            self.configFile = os.path.join(self.dataDir, "config.ini")
            
        # Make sure that we can create the data dir
        if not os.access(self.dataDir, os.F_OK):
            try:
                os.makedirs(self.dataDir, 0744)
            except os.error, e:
                raise SystemExit("Unable to create datadir '" + self.dataDir + "'")

        # Make sure we can write to the data dir
        if not os.access(self.dataDir, os.W_OK):
            raise SystemExit("Datadir must be writeable '" + self.dataDir + "'")

        # Make sure we can write to the config file
        if not os.access(self.configFile, os.W_OK):
            if os.path.isfile(self.configFile):
                raise SystemExit("Config file '" + self.configFile + "' must be writeable.")
            elif not os.access(os.path.dirname(self.configFile), os.W_OK):
                raise SystemExit(
                    "Config file root dir '" + os.path.dirname(self.configFile) + "' must be writeable.")

        # The pidFile is only useful in daemon mode, make sure we can write the file properly
        if self.createPid:
            if self.runAsDaemon:
                pid_dir = os.path.dirname(self.pidFile)
                if not os.access(pid_dir, os.F_OK):
                    sys.exit("PID dir: " + pid_dir + " doesn't exist. Exiting.")
                if not os.access(pid_dir, os.W_OK):
                    sys.exit("PID dir: " + pid_dir + " must be writable (write permissions). Exiting.")

            else:
                # if self.consoleLogging:
                sys.stdout.write("Not running in daemon mode. PID file creation disabled.\n")
                self.createPid = False
                
        os.chdir(self.dataDir)
            
    def daemonize(self):
        if self.runAsDaemon:
            try:
                # set session ID to this process so we can kill group in sigterm handler
                # os.setsid()
                from lib.daemon import Daemon
                self.daemon = Daemon(self.pidFile,
                                    stdin=self.logFile,
                                    stdout=self.logFile,
                                    stderr=self.logFile)
                self.daemon.daemonize()
                self.logger.info("daemonize pid %s" % os.getpid())
            except SystemExit:
                raise
            except:
                self.log.critical(traceback.format_exc())
            
    def run(self):
        self.addSignals()
        PotatoRage(self.dataDir, self.webPort)       

    def addSignals(self):
        # Control+C
        signal.signal(signal.SIGINT, self.onExit)
        
        # stop
        signal.signal(signal.SIGTERM, self.onExit)
        
    def onExit(self, signal, frame):
        self.logger.info("stop")
        sys.exit(1)        
    
if __name__ == "__main__":
    l = None
    # try:
    l = Loader()
    l.daemonize()
    l.run()
    # except:
    #    raise
