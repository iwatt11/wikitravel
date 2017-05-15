# -*- coding: utf-8 -*-#
# !/usr/local/bin/python2.7
import json
import wikipedia
import popularity as wpv
import urllib2
import os
import text as txt

sorry = "There is nothing nearby of interest. Seriously. We checked."


class TownStateWikiData:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.namespace = self.town_and_state()

    def get_geonames(self, types):
        """Collect from Google API geographical names along with their types."""
        url = 'http://maps.googleapis.com/maps/api/geocode/json' + \
              '?latlng={},{}&sensor=false'.format(self.lat, self.lng)
        json_data = json.load(urllib2.urlopen(url))
        address_comps = json_data['results'][0]['address_components']
        filter_method = lambda x: len(set(x['types']).intersection(types))
        return filter(filter_method, address_comps)

    def town_and_state(self):
        """Obtain long Town and State names."""
        types = ['locality', 'administrative_area_level_1']
        namespace = []
        try:
            for geo_name in self.get_geonames( types):
                name = geo_name['long_name']
                namespace.append(name)
                return namespace
            else:
                return False
        except:
            return False

    @staticmethod
    def wiki_townstate(namespace):
        """Get Wiki article associated with Town,_State naming convention. Return dict with sections and text."""
        try:
            if len(namespace) > 1:
                place_url = namespace[0]+',_'+namespace[1]
            else:
                place_url = namespace
            raw = wikipedia.page(place_url).content.encode('utf-8')
            return txt.text_cleaning(raw)
        except:
            return False


class GeoPreciseWikiData:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lon = lng

    def wiki_geosearch(self):
        """Utilizes Wikipedia's geosearch functionality and page views API to return most relevant local info."""
        closeby = []
        radius = 500
        while len(closeby) < 1 and radius <= 10000:
            print("Searching within "+ str(radius) + " metres...")
            closeby = wikipedia.geosearch(self.lat, self.lon, radius=radius)
            radius += 500
        if len(closeby) > 0:
            important = wpv.WikiViews(closeby).sorted
            return txt.clean_sorted(important)
        else:
            os.system("say " + sorry)
            exit()

    @staticmethod
    def get_wikidata(pagename):
        return wikipedia.page(pagename).content.encode('utf-8')
