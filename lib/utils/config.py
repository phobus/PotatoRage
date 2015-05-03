#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

import logging
log = logging.getLogger(__name__)

def _default_settings(base_dir):
    global settings
    settings = {'folders':{}, 'files':{}, 'server':{}}
    
    settings['folders']['cache'] = os.path.join(os.path.join(base_dir, 'data'), 'cache')
    settings['folders']['img'] = os.path.join(os.path.join(base_dir, 'data'), 'img')
    
    settings['files']['db'] = os.path.join(os.path.join(base_dir, 'data'), 'pyster.sqlite')
    settings['files']['log'] = os.path.join(os.path.join(base_dir, 'log'), 'pyster.log')
    
    settings['server']['host'] = '0.0.0.0'
    settings['server']['port'] = 8080
    settings['server']['debug'] = True
    settings['server']['reloader'] = True
       
def _parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Star daemon and web server for Pyster %s the Torrent manager' % '0.6')
    parser.add_argument('--config', help='full path to the file default ./etc/config.ini')
    parser.add_argument('--port', type=int, help='port to listen default 8080')
    parser.add_argument('--host', help='host default 0.0.0.0')
    return parser.parse_args()

def _load_settings(config_file):
    log.debug('Load settings: %s' % config_file)
    parser = ConfigParser.ConfigParser()
    parser.read(config_file)
    opt = None
    for s in parser.sections():
        for o in parser.options(s):
            settings[s][o] = parser.get(s, o)
            
def _save_settings(config_file):
    log.debug('Save settings: %s' % config_file)
    parser = ConfigParser.ConfigParser()
    file = open(config_file, 'w')
    for sk, sv in settings.items():
        parser.add_section(sk)
        for k, v in sv.items():
            parser.set(sk, k, v)
    parser.write(file)
    file.close()
    
def _check_config():
    checkFolder(os.path.dirname(settings['files']['db']))
    if not os.path.isfile(settings['files']['db']):
        log.debug('Creating db')
        from models import connection
        from models.db import exec_script
        sql_dir = os.path.join(os.path.join(base_dir, 'models'), 'sql')
        exec_script(connection, os.path.join(sql_dir, 'schema.sql'))
    
    for file in settings['files'].values():
        checkFolder(os.path.dirname(file))
    for folder in settings['folders'].values():
        checkFolder(folder)

def _config_log():
    import logging
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    
    formatter = logging.Formatter(u'%(asctime)s %(levelname)s::%(message)s', '%H:%M:%S')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
       
def checkFolder(folderpath):
    if not os.access(folderpath, os.F_OK):
        try:
            log.debug('Make dir: %s' % folderpath)
            os.makedirs(folderpath, 0744)
        except os.error, e:
            raise SystemExit("Unable to create '%s'" % folderpath)
    
    if not os.access(folderpath, os.W_OK):
        raise SystemExit("Folder '%s' must be writable " % folderpath)

try:
    settings
except NameError:
    _config_log()
    args = _parse_args()

    base_dir = os.path.realpath('.')
    config_file = args.config if args.config else os.path.join(os.path.join(base_dir, 'etc'), 'config.ini')
    
    _default_settings(base_dir)
        
    if os.path.isfile(config_file):
        _load_settings(config_file)
    else:
        checkFolder(os.path.dirname(config_file))
        _save_settings(config_file)
        
    if args.host:
        settings['server']['host'] = args.host
    
    if args.port:
        settings['server']['port'] = args.port
    
    _check_config()