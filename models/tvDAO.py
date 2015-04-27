#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base_DAO import DAO

class tvDAO(DAO):
    def __init__(self):
        DAO.__init__(self, 'tv')