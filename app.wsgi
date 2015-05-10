# Change working directory so relative paths (and template lookup) work again
import os
os.chdir(os.path.dirname(__file__))

import sys
sys.path.insert(0, os.path.dirname(__file__))

import bottle
# ... build or import your bottle application here ...

# Make sure our bundled libraries take precedence
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib'))

from utils.config import settings
import api, routes, controllers
# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()
