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
    
    def get_torrent3(self, media, query):
        from bs4 import BeautifulSoup
        
        if media == self.media[0]:
            url = self.url_search % query
            print url
            
            opener = urllib2.build_opener(CacheHandler("/home/neganix/git/Pyster/data/cache/"))
            response = opener.open(url)
            data = response.read()
            
            soup = BeautifulSoup(data)
            search_list = soup.find('ul', {'class':'buscar-list'})
            
            print search_list
            for anchor in search_list.find_all('a'):
                print(anchor.get('href', '/')), (anchor.get('title', '/'))
            
    def get_torrent2(self, media, query):
        try:
            import xml.etree.cElementTree as ElementTree
        except ImportError:
            import xml.etree.ElementTree as ElementTree
            
        if media == self.media[0]:
            url = self.url_search % query
            print url
            
            opener = urllib2.build_opener(CacheHandler("/home/neganix/git/Pyster/data/cache/"))
            response = opener.open(url)
            data = response.read()
            
            et = ElementTree.fromstring(data)
            for link in et.iter('a'):
                print link.attrib

    def get_torrent1(self, media, query):
        import re
        
        if media == self.media[0]:
            url = self.url_search % query
            print url
            opener = urllib2.build_opener(CacheHandler("/home/neganix/git/Pyster/data/cache/"))
            #opener = urllib2.build_opener()
            #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            opener.addheaders = [('Accept-Charset', 'iso-8859-1')]
            response = opener.open(url)
            data = response.read().decode('iso-8859-1')
            #print data
            # pattern = r'<a\shref=[\'"]?([^\'" >]+%s)' % query
            # pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
            # pattern = r'(<a.*?>.*?</a>)'
            # pattern = r'(<a.*?>.*?interstellar.*?</a>)'
            # pattern = r'<ul class="buscar-list">.*?</ul>'
            # pattern = r'<\s*\w*\s*href\s*=\s*"?\s*([\w\s%#\/\.;:_-]*)\s*"?.*?>'
            # pattern = r'<ul class="buscar-list">(.*?)<\/ul><!-- end .buscar-list -->'
            pattern = r'(<ul class="buscar-list">(.|\n)*?</ul><!-- end .buscar-list -->)'
            search = re.search(pattern, data)
            if search:
                # print search.group()
                # for item in enumerate(re.findall(pattern, data)):
                # pattern = r'((href|title)=".*?")'
                # pattern = r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))'
                pattern = r'(<a.*?>)'
                html = '<root>'
                for item in re.finditer(pattern, search.group()):
                    print item.group()
                    html += item.group() + '</a>'
                html += '</root>'
                #print html
                try:
                    import xml.etree.cElementTree as ElementTree
                except ImportError:
                    import xml.etree.ElementTree as ElementTree
                
                et = ElementTree.fromstring(html)
                for link in et.iter('a'):
                    print link.attrib
# http://www.dotnetperls.com/scraping-html
# http://stackoverflow.com/questions/12479570/given-a-torrent-file-how-do-i-generate-a-magnet-link-in-python
if __name__ == "__main__":
    newpct1().get_torrent1('movie', 'interstellar')
    pass
