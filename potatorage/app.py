#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
from ui import Notifications, Notification
import webserver
from api import api

class PotatoRage:
    def __init__(self, daemon, home_dir, data_dir, host, port):
        self.daemon = daemon
        self.home_dir = home_dir
        self.data_dir = data_dir
        
        self.host = host
        self.port = port
        
        webserver.HOME_DIR = home_dir
        webserver.DATA_DIR = data_dir
        """self.notifications = Notifications()
        self.api = api(self.notifications)
        
        self.worker = threading.Thread(target=self.work);
        #self.worker.start()
        
        self.bottle = PRBottle(self.home_dir, self.api)
        self.server = MyWSGIRefServer(host=self.host, port=self.port)
        self.bottle.run(server=self.server)"""
        
    def start(self):
        self.webServer.run(host=self.webHost, port=self.webPort)
        
    def work(self):
        i = 0
        while self.daemon.daemon_alive:
            print self.daemon.daemon_alive
            time.sleep(1)
            # self.notifications.message("mensaje %s" % i, 'q ase?')
            # i += 1
            # time.sleep(1)
        self.server.stop()
