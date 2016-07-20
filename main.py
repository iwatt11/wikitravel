import location_model as lm
import sys
import json
import os

def main():
    coords = [34.057348, -118.273674]
    lat = coords[0]
    lng = coords[1]
    instance = lm.GetWikiData(lat, lng)
    print instance.json_response
    #text_dict = wiki_work(namespace)
    sections = []
    for cat, desc in instance.json_response.iteritems():
       sections.append(cat)

    #text_dict_json = json.dumps(instance.json_response)

    summary = instance.json_response['Summary']
    history = instance.json_response['Notable people'].replace('(', '.').replace(')', '.')
    os.system('say %s' % (summary))
    os.system('say %s' % (history))




if __name__ == '__main__':
    sys.exit(main())