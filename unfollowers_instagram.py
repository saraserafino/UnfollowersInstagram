#!/usr/bin/env python3
import json

# Read the JSON files of followers and followings
with open('followers_1.json', 'r') as file:
    followers_data = json.load(file)

with open('following.json', 'r') as file:
    followings_data = json.load(file)

# Create a vector with their nicknames, accordingly to the structure of the files
followers = [entry['value'] for item in followers_data for entry in item['string_list_data']]
followings = [entry['value'] for item in followings_data['relationships_following'] for entry in item['string_list_data']]

def unfollowers(followings, followers):
    print("You follow them but they do not follow you back:\n")
    tot = 0
    for i in followings:
        if i not in followers:
            tot=tot+1
            print(str(tot)+" "+i)
    print("\nTotal: "+str(tot))
        
def fans(followings, followers):
    print("\nThey follow you but you do not follow them:\n")
    tot = 0
    for i in followers:
        if i not in followings:
            tot=tot+1
            print(str(tot)+" "+i)
    print("\nTotal: "+str(tot))

unfollowers(followings, followers)
fans(followings, followers)
