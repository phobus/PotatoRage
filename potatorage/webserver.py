#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from potatorage.setup import *
from potatorage.indexer.series import TheTvDb
from lib.bottle import static_file, request

if not app:
    app = Bottle()
    
def run():
    app.run(host=HOST, port=PORT)

indexer_series = TheTvDb()
    
@app.get('/')
def _index():
    return static_file(INDEX, root=STATIC_DIR)
    
@app.get('/static/<filename:path>')
def _send_static(filename):
    return static_file(filename, root=STATIC_DIR)

# rest api
# indexer

@app.get('/api/idx/series')
def _api_get_idx_series_search():
    # try:
    q = request.query.q
    # except Exception, error:
    return {'series' :indexer_series.search(q)}

@app.get('/api/idx/series/<sid>')
def _api_get_idx_series():
    # try:
    sid = request.query.sid
    print indexer_series.get_by_id(sid)
    # except Exception, error:
    return indexer_series.get_by_id(sid)


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
