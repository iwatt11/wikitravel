# -*- coding: utf-8 -*-#
# !/usr/local/bin/python2.7
import sys
from os import system
import json
import wikipedia
import urllib2
from itertools import izip


class
def wiki_work(namespace):
    """Get Wiki article associated with Town,_State naming convention. Return dict with sections and text."""
    #  wikipedia.geosearch might be a nice add-on later
    try:
        place_url = namespace[0]+',_'+namespace[1]
        text = wikipedia.page(place_url).content.replace("\n", "").encode('utf-8')
        s = text.split('==')
        t = map(str.strip, s)
        t[:0]= [u'Summary']
        i = iter(t)
        text_dict = dict(izip(i,i))

        return text_dict

    except wikipedia.exceptions.DisambiguationError:
        error_message = "No record for your location. Try again on down the road."
        system('say %s' % (error_message))
        sys.exit()


def get_geonames(lat, lng, types):
    """Collect from Google API geographical names along with their types."""
    url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
            '?latlng={},{}&sensor=false'.format(lat, lng)
    json_data = json.load(urllib2.urlopen(url))
    address_comps = json_data['results'][0]['address_components']
    filter_method = lambda x: len(set(x['types']).intersection(types))

    return filter(filter_method, address_comps)

def town_and_state(lat, lng):
    """Obtain long Town and State names."""
    types = ['locality', 'administrative_area_level_1']
    namespace = []
    try:
        for geo_name in get_geonames(lat, lng, types):
            name = geo_name['long_name']
            namespace.append(name)
    except:
        error_message = "No record for your location. Try again on down the road."
        system('say %s' % (error_message))
        sys.exit()

    return namespace


def main():
    lat, lng = 37.158664700000000000, -84.8018970
    namespace = town_and_state(lat, lng)
    print namespace

    text_dict = wiki_work(namespace)
    sections = []
    for cat, desc in text_dict.iteritems():
        sections.append(cat)
    print text_dict
    text_dict_json = json.dumps(text_dict)
    print text_dict_json
    #summary = text_dict['Summary']
    #history = text_dict['Notable people'].replace('(', '.').replace(')', '.')
    #system('say %s' % (summary))
    #system('say %s' % (history))


if __name__ == '__main__':
    sys.exit(main())