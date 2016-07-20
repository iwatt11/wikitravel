import location_model as lm
import sys


def main():
    coords = [34.057348, -118.273674]
    lat = coords[0]
    lng = coords[1]
    instance = lm.GetWikiData(lat, lng)
    #text_dict = wiki_work(namespace)
    #sections = []
    #for cat, desc in text_dict.iteritems():
    #    sections.append(cat)
    #print text_dict
    #text_dict_json = json.dumps(text_dict)
    #print text_dict_json
    #summary = text_dict['Summary']
    #history = text_dict['Notable people'].replace('(', '.').replace(')', '.')
    #system('say %s' % (summary))
    #system('say %s' % (history))




if __name__ == '__main__':
    sys.exit(main())