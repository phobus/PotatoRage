#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    import xml.etree.ElementTree as ElementTree

class TheTvDb:
    """
    http://www.thetvdb.com/wiki/index.php/API:GetSeries
    """
    def __init__(self):
        self.base_url = 'http://thetvdb.com'
        self.language = 'es'
        self.apikey = '0629B785CE550C8D'
        self.url_getSeries = u"%s/api/GetSeries.php?language=%s&seriesname=%%s" % (self.base_url, self.language)
        self.url_seriesInfo = u"%s/api/%s/series/%%s/%%s.xml" % (self.base_url, self.apikey)
        self.url_epInfo = u"%s/api/%s/series/%%s/all/%%s.xml" % (self.base_url, self.apikey)
        
    def search(self, name):
        name = urllib.quote(name.encode("utf-8"))
        url = self.url_getSeries % name;

        response = urllib2.urlopen(url)
        xml = response.read()
        et = ElementTree.fromstring(xml)
        
        allSeries = []
        for series in et:
            result = {}
            for item in series:
                tag = item.tag.lower()
                if tag in ['seriesid', 'language', 'seriesname', 'network']:
                    result[tag] = item.text
            result['seriesid'] = int(result['seriesid'])
            allSeries.append(result)
        return allSeries

    def info(self, sid):
        url = self.url_seriesInfo % (sid, self.language);
        for series in et:
            result = dict((k.tag.lower(), k.text) for k in series.getchildren())
            result['seriesid'] = int(result['seriesid'])
            """if 'aliasnames' in result:
                result['aliasnames'] = result['aliasnames'].split("|")"""
            allSeries.append(result)
            break
        return allSeries