#coding: utf-8

# Python 2.7
# This program is supposed to automatically thank people that write on your Facebook wall during birthdays
# Not currently working (key error supposedly). Work in progress.
# "alreadyThanked" list in case I want to make this program use a while loop that monitors my Facebook wall
# Made by Michel Tabari with inspiration from others

import requests, json
from random import choice
from datetime import datetime

# set your birthday time
bDay = datetime(2015, 5, 27, 01, 00, 0)

epoch = datetime(1970,1,1)
td = bDay - epoch
utc_bday = int((td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 1e6)


# set your fb access token
fbAccessToken'

# list for 'thanks' in Swedish
thanksSwe = ['Tack så mycket! ', 'Tack!']
# list for 'thanks' in English
thanksEng = ['Thank you so much!', 'Thanks!', 'Thank you!']

smileys = [':-)', ':-D']

commonGreetingsSwe = ['Grattis!', 'grattis!', 'grattis', 'Grattis']
commonGreetingsEng = ['Happy', 'birthday', 'Happy!', 'happy', 'happy!', 'birthday!', 'Birthday!']

# to store post_id after thanking persons
alreadyThanked = []

def getPosts():
	fqlQuery = ("""SELECT post_id, actor_id, user_id, message FROM stream 
		WHERE filter_key = 'others' AND source_id = me() AND created_time > 1432688400 LIMIT 200""")
	payload = {'q': fqlQuery, 'access_token': fbAccessToken}
	requestFB = requests.get('https://graph.facebook.com/fql', params = payload)
	result = json.loads(requestFB.text)
	# print result
	# this returns a key error for 'data'
	return result['data']

def thankYou(wallposts):
	for wallpost in wallposts:
			if any(wallpost['message'].strip(" ") in commonGreetingsSwe):
				requestFB = requests.get('https://graph.facebook.com/%s' % (wallpost['actor_id']))
				urlforThanks = 'https://graph.facebook.com/%s/comments' % (wallpost['post_id'])
				user = json.loads(requestFB.text)
				# key 'first_name' doesn't seem to work atm.
				message = '%s %s %s' % (choice(thanksSwe), user['first_name'], choice(smileys))
				payload = {'access_token': fbAccessToken, 'message': message}
				send = requests.post(urlforThanks, data = payload)
				print 'Wall post %s done in Swedish' % (wallpost['post_id'])
				alreadyThanked.append(wallpost['post_id'])
			else:
				requestFB = requests.get('https://graph.facebook.com/%s'% (wallpost['actor_id']))
				urlforThanks = 'https://graph.facebook.com/%s/comments' % (wallpost['post_id'])
				user = json.loads(requestFB.text)
				message = '%s %s %s' % (choice(thanksEng), user['first_name'], choice(smileys))
				payload = {'access_token': fbAccessToken, 'message': message}
				send = requests.post(urlforThanks, data = payload)
				print 'Wall post %s done in English' % (wallpost['post_id'])
				alreadyThanked.append(wallpost['post_id'])


if __name__ == '__main__':
	thankYou(getPosts())
