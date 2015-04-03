#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import sys
import os

from lib.daemon import Daemon

import potatorage
from potatorage.webserver import  WebServer

class Loader(Daemon):
    def run(self):
        while True:
            time.sleep(1)
def main():
    potatorage.MY_FULLNAME = os.path.normpath(os.path.abspath(__file__))
    potatorage.MY_NAME = os.path.basename(potatorage.MY_FULLNAME)
    potatorage.PROG_DIR = os.path.dirname(potatorage.MY_FULLNAME)
    potatorage.DATA_DIR = potatorage.PROG_DIR
    potatorage.MY_ARGS = sys.argv[1:]
    potatorage.DAEMON = False
    potatorage.CREATEPID = False
    
    print 'MY_FULLNAME: ' + potatorage.MY_FULLNAME
    print 'MY_NAME: ' + potatorage.MY_NAME
    print 'PROG_DIR: ' + potatorage.PROG_DIR
    print 'DATA_DIR: ' + potatorage.DATA_DIR
    print 'MY_ARGS: %s' % potatorage.MY_ARGS
    print 'DAEMON: %s' % potatorage.DAEMON
    print 'CREATEPID: %s' % potatorage.CREATEPID
    
    webServer = WebServer()
    webServer.run(host='127.0.0.1', port=8080)

if __name__ == "__main__":
    main()
        
if __name__ == "__main__2":
    daemon = Loader('tmp/potatorage.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
