#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

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

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

api = InstagramAPI("iamjumpmanofficial", "Trilogeekd7!")
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print("\r\nLogin success!")

    s = str(api.LastJson)

    idx1 = 0
    idx2 = -1
    idx1 = s.find("@", idx1)
    while idx1 > 0:
        idx2 = s.find(" ", idx1)
        #print("      idx1= " + str(idx1) + ", idx2= " + str(idx2))
        s2 = s[idx1:idx2]
        print(s2)
        idx1 = s.find("@", idx2)

    print("\r\nWriting output file...")
    f = open("Instagram-output.txt", "w", encoding='utf-8')
    f.write(s)
    f.close()
    # print(api.LastJson)  # print last response JSON

    # user_id = 15503147	# serenawilliams
    user_id = 3280631674	# christhefr 
    followers = getTotalFollowers(api, user_id)
    print('Number of followers:', len(followers))

    #next_max_id = ''
    #followersB = api.getUserFollowers(1623112898, next_max_id)
    #print('Number of followers:', len(followersB))

    mediaId = '2139085373926303794_7932030313'	# a media_id
    recipients = [1623112898]			# array of user_ids. They can be strings or ints
    #api.direct_share(mediaId, recipients, text='iamjumpmanofficial')
else:
    print("\r\nLogin failed!")
