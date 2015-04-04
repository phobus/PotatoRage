#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
from ui import Notifications, Notification
from webserver import WebServer

class PotatoRage:
    def __init__(self, dataDir, webPort):
        self.dataDir = dataDir
        
        self.webHost = '0.0.0.0'
        self.webPort = webPort
        
        self.notifications = Notifications()
        self.notifications.message('hola', 'q ase?')
        
        self.webServer = WebServer(self.dataDir)
        self.webServer.notifications = self.notifications
        
        # self.webServer.run(host=self.webHost, port=self.webPort, quiet=False, debug=None)
        #self.webServer.run(host=self.webHost, port=self.webPort)
        
        self.webThread = threading.Thread(
                                    target=self.webServer.run,
                                    kwargs=dict(host=self.webHost, port=self.webPort)
                                    )
        self.webThread.start()
        
        i = 0
        while (True):
            self.notifications.message("mensaje %s" % i, 'q ase?')
            i += 1
            time.sleep(3)
