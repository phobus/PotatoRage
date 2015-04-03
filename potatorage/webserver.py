#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import potatorage
import os

from lib.bottle.bottle import Bottle, route, run, template, request, static_file, error

class WebServer(Bottle):
    def __init__(self, progDir):
        super(WebServer, self).__init__()
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
        
    def _index(self):
        return static_file(self.index, root=self.webRoot)
    
    def _static_css(self, filepath):
        return static_file(filepath, root=self.cssFolder)
    
    def _static_js(self, filepath):
        return static_file(filepath, root=self.jsFolder)
    
    def _static_img(self, filepath):
        return static_file(filepath, root=self.imgFolder)
