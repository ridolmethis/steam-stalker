#! /usr/bin/python2
import json
import urllib2
import xmltodict

#from steam_stalker import skeletons
#import steam_stalker #skeletons 
from steam_stalker import skeletons

APIKEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
STEAMID = "76561197960435530"

FORMAT = "json"
DEBUG = 0

def printSkeletonTemplate(template):
    order = ['base_url','api_interface_name','api_method_name','api_version','EXTRAS']
    try:
        print 'template_name: \t%s' % template
        for x in order:
            print '%s: \t%s' % (x, template[x])
    except Exception as e:
        print e

def urlFromSkeletonTemplate(_skeletons,key):
    url_template = ['http://','BASE_URL','/','API_INTERFACE_NAME','/','API_METHOD_NAME','/','API_VERSION','/','EXTRAS']
    try:
        skele = _skeletons[key]
        if DEBUG > 0: print SkeletonTemplate(skele)
        for x in skele:
            url_index = url_template.index(x.upper())
            if x == 'EXTRAS':
                extras = '&'.join(skele['EXTRAS']) # add extra url variables. ampersand to seperate
                url_template[url_index] = '?' + extras
                continue
            # replaces placeholder value with value from template.
            # includes APIKEY and STEAMID. generating new skeletons
            # will be necessary to change these values
            url_template[url_index] = skele[x]
        return ''.join(url_template)
    except KeyError as e:
        print '\"%s\" template was not found' % key

skeletons = skeletons.initSkeletons(APIKEY,STEAMID,FORMAT,300)
url = urlFromSkeletonTemplate(skeletons,'GetNewsForApp')


def downloadData(url):
    try:
        print url
        op = urllib2.urlopen(url)
        mess = op.read()
        data = json.loads(mess) #comress mess, reserves memory
        print data
    except Exception as e:
        print "[x] Error %s" % e 

downloadData(url)
