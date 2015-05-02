#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

base_dir = os.path.realpath('.')
data_dir = os.path.join(base_dir, 'data')
sql_dir = patch = os.path.join(os.path.join(base_dir, 'models'), 'sql')

settings = {'folders':{}, 'files':{}, 'server':{}}

settings['folders']['cache'] = os.path.join(data_dir, 'tmp')
settings['folders']['img'] = os.path.join(data_dir, 'img')

settings['files']['db'] = os.path.join(data_dir, 'pyster.sqlite')
# settings['files']['log'] = os.path.join(data_dir, 'pyster.log')

settings['server']['host'] = None
settings['server']['port'] = None
settings['server']['debug'] = True
settings['server']['reloader'] = True
       
def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='Star daemon and web server for Pyster %s the Torrent manager' % '0.6')
    
    # parser.add_argument('--daemon', action='store_true', help='run as daemon')
    # parser.add_argument('--pidfile', help='Combined with --daemon creates a pidfile (full path including filename)')
    
    # parser.add_argument('--datadir', help='full path data folder')
    parser.add_argument('--config', help='full path to the file')
    
    parser.add_argument('--port', type=int, default=8080, help='port to listen default 8080')
    parser.add_argument('--host', default='0.0.0.0', help='host default 0.0.0.0')
    
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument('--start', action='store_true')
    # group.add_argument('--stop', action='store_true')
    # group.add_argument('--restart', action='store_true')
    # group.add_argument('--status', action='store_true')
    
    args = parser.parse_args()
    
    settings['server']['host'] = args.host
    settings['server']['port'] = args.port
    
    config_file = None
    if args.config:
        config_file = args.config
    else:
        config_file = os.path.join(os.path.join(base_dir, 'etc'), 'config.ini')
        
    if os.path.isfile(config_file):
        load_settings(config_file)
    else:
        checkFolder(os.path.dirname(config_file))
        save_settings(config_file)
        checkFolder(data_dir)
        checkFolder(settings['folders']['cache'])
        checkFolder(settings['folders']['img'])
        
    check_config()
        
def load_settings(config_file):
    parser = ConfigParser.ConfigParser()
    parser.read(config_file)
    for s in parser.sections():
        for o in parser.options(s):
            settings[s][o] = parser.get(s, o)
            
def save_settings(config_file):
    parser = ConfigParser.ConfigParser()
    file = open(config_file, 'w')
    for sk, sv in settings.items():
        parser.add_section(sk)
        for k, v in sv.items():
            parser.set(sk, k, v)
    parser.write(file)
    file.close()
    
def check_config():
    if not os.path.isfile(settings['files']['db']):
        from models import connection
        from models.db import exec_script
        exec_script(connection, os.path.join(sql_dir, 'schema.sql'))

def checkFile(filepath):
    if not os.access(filepath, os.W_OK):
        if os.path.isfile(filepath):
            raise SystemExit("File '%s' must be writable." % os.path.dirname(logfile))
        elif not os.access(os.path.dirname(filepath), os.W_OK):
            raise SystemExit("Folder '%s' must be writable." % os.path.dirname(logfile))
    
def checkFolder(folderpath):
    if not os.access(folderpath, os.F_OK):
        try:
            os.makedirs(folderpath, 0744)
        except os.error, e:
            raise SystemExit("Unable to create '%s'" % folderpath)
    
    if not os.access(folderpath, os.W_OK):
        raise SystemExit("Folder '%s' must be writable " % folderpath)
