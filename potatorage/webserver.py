#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import potatorage

from lib.bottle.bottle import Bottle, route, run, template, request, static_file, error

class WebServer(Bottle):
    def __init__(self):
        super(WebServer, self).__init__()
        #home
        self.route('/', callback=self._index)
        self.route('/index.html', callback=self._index)
        #static files
        self.route('/css/<filepath:path>', callback=self._static_css)
        self.route('/js/<filepath:path>', callback=self._static_js)
        self.route('/img/<filepath:path>', callback=self._static_img)
        
    def _index(self):
        return static_file('index.html', root="%s/web/" % potatorage.PROG_DIR)
    
    def _static_css(self, filepath):
        return static_file(filepath, root="%s/web/css/" % potatorage.PROG_DIR)
    
    def _static_js(self, filepath):
        return static_file(filepath, root="%s/web/js/" % potatorage.PROG_DIR)
    
    def _static_img(self, filepath):
        return static_file(filepath, root="%s/web/img/" % potatorage.PROG_DIR)