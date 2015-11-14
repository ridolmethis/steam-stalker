import json
import urllib2

APIKEY = "XXX"
robwalker = "76561197960435530"

def reloadSkeleton(GROUP_TYPE, GROUP_REQUEST, VNUM, API_KEY, STEAM_PLURAL, STEAM_ID):
	fleshedurl = "http://api.steampowered.com/" + GROUP_TYPE + "/" + GROUP_REQUEST + "/" + VNUM + "/?key=" + API_KEY + "&" +STEAM_PLURAL+ "=" + STEAM_ID
	return fleshedurl
	
def getFriendList(STMID):
	#creates url for GetFriendList
	url = reloadSkeleton("ISteamUser", "GetFriendList", "v0001",APIKEY,'steamid',STMID) + '&relationship=friend'
	print url
	try:
		op = urllib2.urlopen(url)
		mess = op.read()
		data = json.loads(mess)
	except Error as e:
		print e
		
	#iterates json for steamids
	friendList = []
	for friend in data["friendslist"]["friends"]:
		friendList.append(str(friend["steamid"]))
	return friendList
	
def getSummaries(idlist,getGameName=False,getRealName=False,getCountry=False,getClanId=False): #can be used to recieve info about friends
	nameList = []
	rNameList = []
	placeList = []
	clanList = []
	
	print 'gathering data for ' + str(len(idlist))
	for id in idlist:
		#creates url for GetPlayerSummaries
		url = reloadSkeleton('ISteamUser','GetPlayerSummaries','v0002',APIKEY,'steamids',id)
		op = urllib2.urlopen(url)
		mess = op.read()
		data = json.loads(mess)	
		
		print 'received data of ' + id 
		
		#iterates json for ign
		if getGameName:
			for name in data['response']['players']:
				nameList.append(name['personaname'])
		
		#iterates json for realname
		if getRealName:
			for rname in data['response']['players']:
				try:
					rNameList.append(rname['realname'])
				except:
					rNameList.append("null")
					
		#iterates	json for country
		if getCountry:
			for country in data['response']['players']:
				try:
					placeList.append(country['loccountrycode'])
				except:
					placeList.append("null")
		#iterates...you get the point
		if getClanId:
			for clan in data['response']['players']:
				try:
					clanList.append(clan['primaryclanid'])
				except:
					clanList.append("null")
	return nameList, rNameList, placeList, clanList

flist = getFriendList(me)

#retrieves info on user based on steamid, accepts a list of steamid
namelist,realnamelist,placelist,clanlist = getSummaries(flist,getGameName=True,getRealName=True,getCountry=True,getClanId=True)
print namelist
