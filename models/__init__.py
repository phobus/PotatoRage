#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db import create_con, exec_script
# exec_script('/home/neganix/git/Pyster/models/sql/schema.sql')
connection = create_con()

from base_DAO import DAO
from movieDAO import movieDAO
from tvDAO import tvDAO

movieDAO = movieDAO(connection)
tvDAO = tvDAO(connection)
episodeDAO = DAO('episode', connection)
