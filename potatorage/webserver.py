#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

# from potatorage.ui import Notifications
import os

from lib.bottle import Bottle, ServerAdapter, static_file, request

from ui import Notifications, Notification

class MyWSGIRefServer(ServerAdapter):
    # server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # self.server.server_close() <--- alternative but causes bad fd exception
        self.server.shutdown()
        
class PRBottle(Bottle):
    def __init__(self, progDir, api):
        super(PRBottle, self).__init__()
        self.api = api
        
        self.webRoot = os.path.join(progDir, 'web')

        self.index = 'index.html'
        self.cssFolder = os.path.join(self.webRoot, 'css')
        self.jsFolder = os.path.join(self.webRoot, 'js')
        self.imgFolder = os.path.join(self.webRoot, 'img')
       
        # home
        self.route('/', callback=self._index)
        self.route('/index.html', callback=self._index)
        # static files
        self.route('/css/<filepath:path>', callback=self._static_css)
        self.route('/js/<filepath:path>', callback=self._static_js)
        self.route('/img/<filepath:path>', callback=self._static_img)
        # notifications
        self.route('/notifications', callback=self._notifications)
        # notifications
        self.route('/api/GetSeries/<seriesname>', callback=self._getSeries)
        
    def _index(self):
        return static_file(self.index, root=self.webRoot)
    
    def _static_css(self, filepath):
        return static_file(filepath, root=self.cssFolder)
    
    def _static_js(self, filepath):
        return static_file(filepath, root=self.jsFolder)
    
    def _static_img(self, filepath):
        return static_file(filepath, root=self.imgFolder)

    def _notifications(self):
        return self.api.getNotifications()
    
    def _getSeries(self, seriesname):
        print seriesname
        #r = requests.get('http://thetvdb.com/api/GetSeries.php?language=es&seriesname=' + seriesname)
        #return r.content
        return self.api.getSeriesFromTheTvDb(seriesname)
