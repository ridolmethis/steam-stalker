#! /usr/bin/python2
import json
import urllib2
import xmltodict

APIKEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
profile = "76561197960435530"

def reloadSkeleton(HEAD, GROUP_TYPE, GROUP_REQUEST, VNUM, API_KEY, STEAM_PLURAL, STEAM_ID):
	if HEAD == 'api.steampowered.com': # for using the steam api
		fleshedurl = "http://" + HEAD + "/" + GROUP_TYPE + "/" + GROUP_REQUEST + "/" + VNUM + "/?key=" + API_KEY + "&" +STEAM_PLURAL+ "=" + STEAM_ID
	else: # when using the steampowered site
		fleshedurl = "http://" + HEAD + "/" + GROUP_TYPE + "/" + GROUP_REQUEST + "/" + VNUM  + "?tab=all&xml=1"
	return fleshedurl
	
def getFriendList(STMID):
	#creates url for GetFriendList
	url = reloadSkeleton("api.steampowered.com", "ISteamUser", "GetFriendList", "v0001",APIKEY,'steamid',STMID) + '&relationship=friend'
	print url
	try:
		op = urllib2.urlopen(url)
		mess = op.read()
		data = json.loads(mess)
		
		#iterates json for steamids
		friendList = []
		for friend in data["friendslist"]["friends"]:
			friendList.append(str(friend["steamid"]))
		return friendList
	except Exception as e:
		print 'something went wrong..\n'
		print e

def gameThief(idlist):
	for id in idlist:
		#creates url for GetOwnedGames 
		url = reloadSkeleton("steamcommunity.com",'profiles', id,'games/',None, None,None) 
		print url
		op = urllib2.urlopen(url)
		mess = op.read()
		#print mess ##Enable for debugging
		
		data = xmltodict.parse(mess)
		print str(data['gamesList']['steamID'])

flist = getFriendList(profile)
gameThief(flist)
