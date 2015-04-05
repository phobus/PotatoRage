#!/usr/bin/env python
# -*- coding: utf-8 -*-

from indexer.thetvdb import TheTvDb

class api:
    RESULT_SUCCESS = 10  # only use inside the run methods
    RESULT_FAILURE = 20  # only use inside the run methods
    RESULT_TIMEOUT = 30  # not used yet :(
    RESULT_ERROR = 40  # only use outside of the run methods !
    RESULT_FATAL = 50  # only use in Api.default() ! this is the "we encountered an internal error" error
    RESULT_DENIED = 60  # only use in Api.default() ! this is the access denied error

    result_type_map = {RESULT_SUCCESS: "success",
                  RESULT_FAILURE: "failure",
                  RESULT_TIMEOUT: "timeout",
                  RESULT_ERROR: "error",
                  RESULT_FATAL: "fatal",
                  RESULT_DENIED: "denied",
                   }
    
    def __init__(self, notifications):
        self.notifications = notifications
        self.tvDb = TheTvDb()
        
    def getNotifications(self):
        messages = []
        for cur_notification in self.notifications.get_notifications():
            messages.append({"title": cur_notification.title,
                           "message": cur_notification.message,
                           "type": cur_notification.type})
        return self._responds(api.RESULT_SUCCESS, messages)
    
    def getSeriesFromTheTvDb(self, seriesname):
        dict = self.tvDb.search(seriesname)
        return self._responds(api.RESULT_SUCCESS, dict)
        
    def _responds(self, result_type, data=None, msg=""):
        """
        result is a string of given "type" (success/failure/timeout/error)
        message is a human readable string, can be empty
        data is either a dict or a array, can be a empty dict or empty array
        """
        if data is None:
            data = {}
        return {"result": api.result_type_map[result_type],
                "message": msg,
                "data": data}