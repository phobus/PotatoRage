#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Set default logging handler to avoid "No handler found" warnings.
import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
#handler = logging.FileHandler('log/pyster.log')
#formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
formatter = logging.Formatter('%(levelname)s - %(name)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)   