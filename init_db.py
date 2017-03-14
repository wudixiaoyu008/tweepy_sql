import sqlite3

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

if reset:
	cur.execute("DROP TABLE IF EXISTS Tweets")
	cur.execute("DROP TABLE IF EXISTS Hashtags")
	cur.execute("DROP TABLE IF EXISTS Tweet_hash")


# Create a table to store Tweets
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, '
table_spec += 'tweet_id INTEGER, tweet_text TEXT, likes INTEGER)'
cur.execute(table_spec)

# Create a table to store Hashtags
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Hashtags (hashtag_id INTEGER PRIMARY KEY AUTOINCREMENT, '
table_spec += 'hashtag_text TEXT, num_occurrences INTEGER)'
cur.execute(table_spec)

# Do you need a third table?
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Tweet_hash ('
table_spec += 'tweet_text TEXT, hashtag_id INTEGER, FOREIGN KEY(hashtag_id) REFERENCES Hashtags(hashtag_id))'
cur.execute(table_spec)
