#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from potatorage import setup
from potatorage.setup import app
from potatorage.indexer.themoviedb import TheMovieDb

from lib.bottle import Bottle, static_file, request

if not app:
    app = Bottle()
    
def run():
    app.run(host=setup.HOST, port=setup.PORT)

# indexer_series = TheTvDb()
    
@app.get('/')
def _index():
    return static_file(setup.INDEX, root=setup.STATIC_DIR)
    
@app.get('/st/<filename:path>')
def _send_static(filename):
    return static_file(filename, root=setup.STATIC_DIR)

# rest api
# indexer

@app.get('/api/idx/movie')
def _idx_search_movies():
    # try:
    query = request.query.q
    # except Exception, error:
    return TheMovieDb().search_movies(query)

@app.get('/api/idx/movie/<id>')
def _idx_get_movie(id):
    # try:
    # except Exception, error:
    return TheMovieDb().get_movie(id)

@app.get('/api/idx/serie')
def _idx_search_serie():
    # try:
    query = request.query.q
    # except Exception, error:
    return TheMovieDb().search_series(query)

@app.get('/api/idx/serie/<id>')
def _idx_get_serie(id):
    # try:
    # except Exception, error:
    return TheMovieDb().get_serie(id)

"""class MyWSGIRefServer(ServerAdapter):
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
        self.server.shutdown()"""
