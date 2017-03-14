import sqlite3
import json

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

f = open('tweets.json')
for line in f:
    line = json.loads(line)
    none = None
    tweet_id = line['id']
    tweet_text = line['text']
    likes = line['favorite_count']
    argument = (none, tweet_id, tweet_text, likes)
    # tweets_item.append(argument)
    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?)'
    cur.execute(statement, argument)
    conn.commit()

f.close()


f1 = open('tweets.json')
hashtag_dic = dict()
for line in f1:
    line = json.loads(line)
    if len(line['entities']['hashtags'])>0:
        for item in line['entities']['hashtags']:
            hashtag_dic[item['text']] = hashtag_dic.get(item['text'], 0) + 1

for k,v in hashtag_dic.items():
    none = None
    argument = (none, k, v)
    statement = 'INSERT INTO Hashtags VALUES (?, ?, ?)'
    cur.execute(statement, argument)
    conn.commit()

f1.close()


query = 'SELECT tweet_text FROM Tweets'
cur.execute(query)

table1 = []
for row in cur:
    table1.append(row[0])


query = 'SELECT hashtag_text FROM Hashtags'
cur.execute(query)

table2 = []
for row in cur:
    table2.append(row[0])


for item in table1:
    for tag in table2:
        if item.find(tag) > 0:
            query = 'SELECT hashtag_id FROM Hashtags WHERE hashtag_text=\'' + tag + '\''
            cur.execute(query)
            for row in cur:
                par_hash = row[0]
                argument = (item, par_hash)
                statement = 'INSERT INTO Tweet_hash VALUES (?, ?)'
                cur.execute(statement, argument)
                conn.commit()
