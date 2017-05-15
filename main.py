import wikiwork as lm
import sys
import text as txt
import subprocess


def main():
    #  Coordinates would be passed from mobile device, etc.
    coords = []
    lat = coords[0]
    lng = coords[1]

    geo_precise = lm.GeoPreciseWikiData(lat, lng)
    closeby_stuff = geo_precise.wiki_geosearch()
    intro = 'Closest Landmarks to Your Location: '
    subprocess.call('say %s' % txt.shellquote(intro), shell=True)
    print('\n' + intro + '\n')

    for rank, close in enumerate(closeby_stuff, start=1):
        print("# " + str(rank) + ": " + close + '\n')
        subprocess.call('say %s' % txt.shellquote(close), shell=True)
        data = geo_precise.get_wikidata(close)
        text = txt.remove_reference_sections(txt.text_cleaning(data))
        summary = text['Summary']
        subprocess.call('say %s' % txt.shellquote(summary), shell=True)


if __name__ == '__main__':
    sys.exit(main())