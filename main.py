import json
import urllib2

APIKEY = ""

def reloadSkeleton(STEAM_ID, STEAM_PLURAL, GROUP_TYPE, GROUP_REQUEST, VNUM, API_KEY=APIKEY):
	fleshedurl = " http://api.steampowered.com/" + GROUP_TYPE + "/" + GROUP_REQUEST + "/" + VNUM + "/?key=" + API_KEY + "&" +STEAM_PLURAL+ "=" + STEAM_ID
	return fleshedurl
	
def getFriendList(STMID):
	#creates url for GetFriendList
	url = reloadSkeleton(STMID, 'steamid', "ISteamUser", "GetFriendList", "v0001")
	print url + '&relationship=friend'
	op = urllib2.urlopen(url)
	mess = op.read()
	data = json.loads(mess)
	
	#iterates json for steamids
	friendList = []
	for friend in data["friendslist"]["friends"]:
		friendList.append(str(friend["steamid"]))
	return friendList
	
def getSummaries(idlist,getGameName=False,getRealName=False,getCountry=False): #can be used to recieve info about friends
	nameList = []
	for id in idlist:
		#creates url for GetPlayerSummaries
		url = reloadSkeleton(id, 'steamids', 'ISteamUser','GetPlayerSummaries','v0002')
		op = urllib2.urlopen(url)
		mess = op.read()
		data = json.loads(mess)	
		
		#iterates json for ign
		if getGameName:
			for name in data['response']['players']:
				#print name['personaname']
				nameList.append(name['personaname'])
	return nameList
#retrievs friend list of target
flist = getFriendList("")
#retrieves names of people on targets friend list
#print getSummaries(flist,getGameName=True)
