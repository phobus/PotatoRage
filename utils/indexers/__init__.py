#!/usr/bin/env python
# -*- coding: utf-8 -*-

idx = {}

from themoviedb import TheMovieDb
tmdb = TheMovieDb()

idx[tmdb.name] = tmdb


