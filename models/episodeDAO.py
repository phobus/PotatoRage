#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_DAO import DataAccess

class episodeDAO(DataAccess):
    def __init__(self, con):
        DAO.__init__(self, 'episode', con)