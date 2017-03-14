import sqlite3
import json

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

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
