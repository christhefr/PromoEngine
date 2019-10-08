#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
import sys, json, os
import requests
import datetime
import time
from InstagramAPI import InstagramAPI


def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _= api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def get_id(username):
    url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+username+"&rank_token=0.3953592318270893&count=1"
    response = requests.get(url)
    respJSON = response.json()
    try:
	    user_id = str( respJSON['users'][0].get("user").get("pk") )
	    return user_id
    except:
	    return "Unexpected error"


api = InstagramAPI("iamjumpmanofficial", "Trilogeekd7!")
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print("\r\nLogin success!")

    s = open("C:/Users/v784707/Downloads/PromoEngine-master/HiphopSearch.txt", "r")
    s = str(s.read())

    # build user list from instagram search or web scrape
    count = 0 # count users found in search
    #users = ['christhefr']
    users = [ t for t in s.split() if t.startswith('@') ]

    print("\r\nWriting output file...")
    f = open("Instagram-output.txt", "a", encoding='utf-8')
    
    for user in users:
        # remove all characters starting at backslashes
        result = user.find("\\")
        if result > 0:
            remchar = user[result:len(user)]
            user = user.replace(remchar,"")
            
        # remove all characters starting at "
        result = user.find('\"')
        if result > 0:
            remchar = user[result:len(user)]
            user = user.replace(remchar,"")

        # if user only has @ sign then remove
        if len(user) != 1:
            mediaId = '2139085373926303794_7932030313'	# a media_id
            userid = get_id(user)
            recipients = [userid]			# array of user_ids. They can be strings or ints
            msg = 'Whats good.. I\'ve been searching the internet all day for people that might like my video. Please take a look when you have chance and feedback would be appreciated. Thx JumpMan'

            try:
                api.direct_share(mediaId, recipients, text=msg)
                s = str(datetime.datetime.now().ctime()) + "," + user + "," + get_id(user) + ",True \n"
                f.write(s)
            except:
                print("Limit reached, bot needs to sleep for 5 minutes.")
                # Wait for 5 minutes
                time.sleep(300)                    
            print("Sending message to username: " + user + " userid: " + userid)
            count = count + 1

    f.close()
    print("Found..." + str(count) + " users in search.")

else:
    print("\r\nLogin failed!")
