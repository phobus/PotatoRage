import urllib
import urllib2

base_url = 'http://api.themoviedb.org/3/search/%s?api_key=%s&language=es&query=%s';
api_key = '28eeb03a21186cf0512bfd1d11ce829e';

def indexer_search(type, query):
    query = urllib.quote(query.encode("utf-8"))
    url = base_url % (type, api_key, query)
    print url
    
    response = urllib2.urlopen(url)
    json = response.read()
    print json
    return json
