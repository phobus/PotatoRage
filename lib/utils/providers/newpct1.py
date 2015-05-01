#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://www.newpct1.com/descarga-torrent/pelicula/%s
http://www.newpct1.com/descarga-torrent/serie/%s

http://tumejorjuego.com/download/index.php?link=%s

https://github.com/skasi7/htpc/blob/master/flexget/urlrewrite_newpct.py
"""
import urllib2

from base_provider import Povider

class newpct1(Povider):
    def __init__(self):
        Povider.__init__(self, 'newpct1', 'https://www.newpct1.org/', ('movie', 'tv'))
        self.base_url = u'http://www.newpct1.com/'
        
        self.url_movie = u'%s/pelicula/%%s/' % self.base_url
        self.url_movie_torrent = u'%s/descarga-torrent/pelicula/%%s/' % self.base_url
        
        self.url_tv = u'%s/series/%%s' % self.base_url
        self.url_ep = u'%s/serie/%%s/capitulo-' % self.base_url
        self.url_ep_torrent = u'%s/descarga-torrent/serie/%%s/capitulo-' % self.base_url

    def get_torrent(self, media):
        if media == self.media[0]:
            
            url = 'http://tumejorjuego.com/download/index.php?link=descargar-torrent/066964_desconexion-blurayrip-ac3-51.html'
            response = urllib2.urlopen(url)
            data = response.read()
            print data

#http://stackoverflow.com/questions/12479570/given-a-torrent-file-how-do-i-generate-a-magnet-link-in-python
if __name__ == "__main__":
    newpct1().get_torrent('movie')