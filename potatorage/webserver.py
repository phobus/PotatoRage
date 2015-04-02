#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import potatorage

from lib.bottle.bottle import Bottle, route, run, template, request, static_file, error

class WebServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._app = Bottle()
        self._route()
    
    def _route(self):
        self._app.route('/', callback=self._index)
        self._app.route('/index.html', callback=self._index)
        self._app.route('/css/<filepath:path>', callback=self._static_css)
        self._app.route('/js/<filepath:path>', callback=self._static_js)
        self._app.route('/img/<filepath:path>', callback=self._static_img)

    def start(self):
        self._app.run(host=self._host, port=self._port)
        
    def _index(self):
        return static_file('index.html', root="%s/web/" % potatorage.PROG_DIR)
    
    def _static_css(self, filepath):
        return static_file(filepath, root="%s/web/css/" % potatorage.PROG_DIR)
    
    def _static_js(self, filepath):
        return static_file(filepath, root="%s/web/js/" % potatorage.PROG_DIR)
    
    def _static_img(self, filepath):
        return static_file(filepath, root="%s/web/js/" % potatorage.PROG_DIR)