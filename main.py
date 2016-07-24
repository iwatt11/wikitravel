import wikiwork as lm
import sys
import text as txt
import os


# def structure_data(self):
#     if self.namespace:
#         raw_wiki = self.wiki_work(self.namespace)
#         if raw_wiki:
#             text_dict = self.text_cleaning(raw_wiki)
#             # To be moved into iPhone application to display section headers
#             # sections = []
#             # for cat, desc in text_dict.iteritems():
#             #    sections.append(cat)
#             self.json_response = json.dumps(text_dict)
#         else:
#             self.json_response = sorry
#     else:
#         self.json_response = sorry
#
#         os.system("say " + sorry)
#         most_important = important[0][0]  # This won't be needed once you let users select. Could be default.

def main():
    coords = [38.078152, 20.790855]
    lat = coords[0]
    lng = coords[1]

    town = lm.TownStateWikiData(lat, lng)
    text = town.wiki_townstate(town.namespace)
    if text:
        summary = text['Summary']
        os.system('say %s' % (txt.say_clean(summary)))

    geo_precise = lm.GeoPreciseWikiData(lat, lng)
    closeby_stuff = geo_precise.wiki_geosearch()
    print closeby_stuff
    os.system('say %s' % (txt.say_clean(closeby_stuff[0])))
    text = geo_precise.get_wikidata(closeby_stuff[0])
    os.system('say %s' % (txt.say_clean(text)))
    exit()


if __name__ == '__main__':
    sys.exit(main())