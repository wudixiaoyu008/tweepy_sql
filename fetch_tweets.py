import tweepy
from tweepy import OAuthHandler
import json

from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# Fetch Taylor Swift's 300 most recent tweets and save them to tweets.json
# with open('tweets.json', 'w') as json_file:
# 	page = 1
# 	while True:
# 		tweets = api.user_timeline(screen_name = 'taylorswift13', count = 300, page = 2) #, include_rts = True
# 		# insert code here to fetch tweets
# 		if tweets:
# 			for tweet in tweets:
# 				# Make sure you limit the number of tweets to 300.
#
# 				json_tweet = json.dumps(tweet._json) # convert to JSON format
# 				json_file.write(json_tweet)
# 				json_file.write('\n')
# 				# Write the tweet to tweets.json
# 		else:
# 			break
# 		page += 1

		# Make sure you limit the number of tweets to 300.


with open('tweets.json', 'w') as json_file:
	for tweet in tweepy.Cursor(api.user_timeline, id="taylorswift13").items(300):
    	# process status here
		json_tweet = json.dumps(tweet._json)
		json_file.write(json_tweet)
		json_file.write('\n')
