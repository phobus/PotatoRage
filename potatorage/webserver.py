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

RESULT_SUCCESS = 10  # only use inside the run methods
RESULT_FAILURE = 20  # only use inside the run methods
RESULT_TIMEOUT = 30  # not used yet :(
RESULT_ERROR = 40  # only use outside of the run methods !
RESULT_FATAL = 50  # only use in Api.default() ! this is the "we encountered an internal error" error
RESULT_DENIED = 60  # only use in Api.default() ! this is the acces denied error

result_type_map = {
    RESULT_SUCCESS: 'success',
    RESULT_FAILURE: 'failure',
    RESULT_TIMEOUT: 'timeout',
    RESULT_ERROR: 'error',
    RESULT_FATAL: 'fatal',
    RESULT_DENIED: 'denied'
}

def result(result_type, data=None, msg=""):
    """
    result is a string of given "type" (success/failure/timeout/error)
    message is a human readable string, can be empty
    data is either a dict or a array, can be a empty dict or empty array
    """    
    if data is None:
        data = {}
        
    return {"result": result_type_map[result_type],
            "message": msg,
            "data": data}
    
@app.route('/')
def _index():
    return static_file(INDEX, root=STATIC_DIR)
    
@app.route('/static/<filename:path>')
def _send_static(filename):
    return static_file(filename, root=STATIC_DIR)
  
@app.route('/api/series/search')
def _api_series_search():
    #try:
    name = request.query.name
    r = result(RESULT_SUCCESS, indexer_series.search(name))
    #except Exception, error:
    #    r = result(RESULT_ERROR, None, "Exception:%s e:%s" % (Exception, error))
    return r

@app.route('/api/series/info')
def _api_series_search():
    #try:
    sid = request.query.sid
    r = result(RESULT_SUCCESS, indexer_series.info(sid))
    #except Exception, error:
    #    r = result(RESULT_ERROR, None, "Exception:%s e:%s" % (Exception, error))
    return r