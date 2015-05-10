#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.newpct1.com/descarga-torrent/pelicula/%s
http://www.newpct1.com/descarga-torrent/serie/%s

http://tumejorjuego.com/download/index.php?link=%s

https://github.com/skasi7/htpc/blob/master/flexget/urlrewrite_newpct.py
"""
import urllib2
import lxml

import sys 
sys.path.insert(0, '/home/neganix/git/Pyster/lib')

from tvdb_cache import CacheHandler

from base_provider import Povider

class newpct1(Povider):
    def __init__(self):
        Povider.__init__(self, 'newpct1', 'https://www.newpct1.org', ('movie', 'tv'))
        self.base_url = u'http://www.newpct1.com'
        
        self.url_movie = u'%s/pelicula/%%s/' % self.base_url
        self.url_movie_torrent = u'%s/descarga-torrent/pelicula/%%s/' % self.base_url
        
        self.url_tv = u'%s/series/%%s' % self.base_url
        self.url_ep = u'%s/serie/%%s/capitulo-' % self.base_url
        self.url_ep_torrent = u'%s/descarga-torrent/serie/%%s/capitulo-' % self.base_url

        self.url_search = u'%s/index.php?page=buscar&q=%%s&ordenar=Nombre&inon=Ascendente' % self.base_url

        self.category_movie = 757
        self.category_tv = 767
        
        self.page_results = 30
        
    def get_torrent(self, media, query):
        import re
        
        if media == self.media[0]:
            url = self.url_search % query
            print url
            opener = urllib2.build_opener(CacheHandler("/home/neganix/git/Pyster/data/cache/"))
            response = opener.open(url)
            data = response.read().decode('iso-8859-1').encode('utf8')

            pattern = r'\( \d+ \) Resultados encontrados'
            search = re.search(pattern, data)
            results = int(search.group().split()[1])
            print results, int(round(float(results) / self.page_results))
            return
        
            pattern = r'(<ul class="buscar-list">(.|\n)*?</ul><!-- end .buscar-list -->)'
            search = re.search(pattern, data)
            if search:
                pattern = r'(<a.*?>)'
                html = '<p>'
                for item in re.finditer(pattern, search.group()):
                    html += '%s</a>' % item.group()
                html += '</p>'
                
                try:
                    import xml.etree.cElementTree as ElementTree
                except ImportError:
                    import xml.etree.ElementTree as ElementTree
                
                et = ElementTree.fromstring(html)
                output = {}
                for link in et.iter('a'):
                    output[link.attrib['href']] = link.attrib['title'].strip()
                for k, v in output.items():
                    print 'k:%s, v:%s' % (k, v)

if __name__ == "__main__":
    newpct1().get_torrent('movie', 'juego de tronos')
    pass
