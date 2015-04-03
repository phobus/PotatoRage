#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import sys
import os
import signal
import logging

import getopt
import time

import potatorage
from potatorage.webserver import  WebServer
# from potatorage.core.logger import PRLog

class Loader:
    def __init__(self):
        self.configFile = None
        self.dataDir = None
        self.progDir = None
        
        self.runAsDaemon = False
        self.createPid = False
        self.pidFile = None
        self.daemon = None
        
        self.webHost = '0.0.0.0'
        self.webPort = '8080'

        self.onInit()
        
        # create logger with 'spam_application'
        self.logger = logging.getLogger('potatorage')
        self.logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(os.path.join(self.dataDir, 'potatorage.log'))
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
        
    def help_message(self):
        return "Usage: TO DO"
            
    def onInit(self): 
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
            sys.exit(self.help_message())
            
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
        
        # Get PID
        # sickbeard.PID = os.getpid()
        
        # self.startWebServer()
        
        # main loop
        # while (True):
            # time.sleep(1)
            
    def daemonize(self):
        if self.runAsDaemon:
            try:
                from lib.daemon import Daemon
                self.daemon = Daemon(self.pidFile)
                self.daemon.daemonize()
                self.logger.info("daemonize pid %s" % os.getpid())
            except SystemExit:
                raise
            except:
                self.log.critical(traceback.format_exc())
            
    def run(self):
        self.addSignals()
        self.startWebServer()
        
    def addSignals(self):
        signal.signal(signal.SIGINT, self.onExit)
        signal.signal(signal.SIGTERM, lambda signum, stack_frame: sys.exit(1))

        # from couchpotato.core.event import addEvent
        # addEvent('app.do_shutdown', self.setRestart)
    
    def onExit(self, signal, frame):
        # from couchpotato.core.event import fireEvent
        # fireEvent('app.shutdown', single = True)
        print "signal%s frame%s"
                          
    def startWebServer(self):
        webServer = WebServer(self.progDir)
        webServer.run(host=self.webHost, port=self.webPort)
    
    
if __name__ == "__main__":
    l = None
    #try:
    l = Loader()
    l.daemonize()
    l.run()
    #except:
    #    raise
