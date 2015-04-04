#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Notifications(object):
    MESSAGE = 'notice'
    ERROR = 'error'
    """
    A queue of Notification objects.
    """
    def __init__(self):
        self._messages = []
        self._errors = []

    def message(self, title, message=''):
        """
        Add a regular notification to the queue

        title: The title of the notification
        message: The message portion of the notification
        """
        self._messages.append(Notification(title, message, Notifications.MESSAGE))

    def error(self, title, message=''):
        """
        Add an error notification to the queue

        title: The title of the notification
        message: The message portion of the notification
        """
        self._errors.append(Notification(title, message, ERROR))
        
    def get_notifications(self, remote_ip='127.0.0.1'):
        return self._messages
  
class Notification(object):
    def __init__(self, title, message='', type=None, timeout=None):
        self.title = title
        self.message = message
        self.type = type