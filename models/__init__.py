#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import create_con, exec_script
connection = create_con()

from base_DAO import DAO
from movieDAO import movieDAO
from tvDAO import tvDAO

movieDAO = movieDAO(connection)
tvDAO = tvDAO(connection)
episodeDAO = DAO('episode', connection)
