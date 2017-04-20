def initSkeletons(_APIKEY,_STEAMID,_FORMAT,_APPID,_COUNT=1,_MAXLENGTH=100):
#initialize this everytime a different user is wanted
    #dictionary contains keys named after value wanted, API naming scheme
    #references second dict, includes HEAD,GROUP_TYPE,VNUM,STEAM_PLURAL
    #dict contains key EXTRAS, value is list of extra strings to append.
    #see the GetFriendList for example, needs '&relationship=friend"
    #skeletons is the wrapper for all templates
    #create a template with the naming scheme $APIMETHOD_Template
    #then update skeletons to include
    skeletons = { }

    getFriendList_Template = { 'GetFriendList': {'base_url':'api.steampowered.com',
                'api_interface_name':'ISteamUser',
                'api_method_name':'GetFriendList',
                'api_version':'v0001',
                'EXTRAS':['key='+_APIKEY,'steamid='+_STEAMID,'realationship=friend','format='+_FORMAT],
                }
            }
    skeletons.update(getFriendList_Template)

    getNewsForApp_Template = {'GetNewsForApp': {'base_url':'api.steampowered.com',
                'api_interface_name':'ISteamNews',
                'api_method_name':'GetNewsForApp',
                'api_version':'v0002',
                'EXTRAS':['appid='+str(_APPID),'count='+str(_COUNT),'maxlength='+str(_MAXLENGTH),'format='+_FORMAT]
                }
            }
    skeletons.update(getNewsForApp_Template)
    return skeletons