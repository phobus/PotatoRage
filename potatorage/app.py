#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
from ui import Notifications, Notification
from webserver import WebServer
from api import api

class PotatoRage:
    def __init__(self, home_dir, data_dir, host, port):
        self.home_dir = home_dir
        self.data_dir = data_dir
        
        self.host = host
        self.port = port
        
        
        self.notifications = Notifications()
        self.api = api(self.notifications)
        
        self.webServer = WebServer(self.home_dir, self.api)

        # self.webServer.run(host=self.webHost, port=self.webPort, quiet=False, debug=None)
        # self.webServer.run(host=self.webHost, port=self.webPort)
        
        self.webWorker = threading.Thread(
                                    target=self.webServer.run,
                                    kwargs=dict(host=self.host, port=self.port)
                                    )
        self.webWorker.start()
        #t = threading.Thread(target=self.work);
        #t.start()
        while True:
            pass
        
    def start(self):
        self.webServer.run(host=self.webHost, port=self.webPort)
        
    def work(self):
        i = 0
        while True:
            pass
            #self.notifications.message("mensaje %s" % i, 'q ase?')
            #i += 1
            #time.sleep(1)
