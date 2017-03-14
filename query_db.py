import sqlite3
import json

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

def most_common_hashtags():
    print ('Most common hashtags:')
    query = 'SELECT hashtag_text, num_occurrences FROM Hashtags'
    cur.execute(query)
    hashtag_list = []
    for row in cur:
        hashtag_list.append(row)
    hashtag_dict = dict(hashtag_list)
    sorted_tag = sorted(hashtag_dict.items(), key=lambda v: v[1], reverse = True)
    for item in sorted_tag[:20]:
        print (item[0])

most_common_hashtags()

def fifty_shades_darker():
    print ('Tweets containing #fiftyshadesdarker :')
    query = 'SELECT Tweets.tweet_id, Tweets.tweet_text FROM Tweets JOIN Hashtags JOIN Tweet_hash ON Tweets.tweet_text = Tweet_hash.tweet_text AND Tweet_hash.hashtag_id = Hashtags.hashtag_id WHERE hashtag_text = \'fiftyshadesdarker\''
    cur.execute(query)
    for row in cur:
        print (row[0], row[1])





fifty_shades_darker()
