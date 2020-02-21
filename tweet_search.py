import os
import tweepy as tw
import pandas as pd

consumer_key= 'zVbaWqBWnwmjTNdrBZL1hgEIP'
consumer_secret= '4cYkREEqpMjxeiZXbxum3RyzdScV7IbaatCT7Gez8OaUNyP1qK'
access_token= '1228048111295246337-nqZwZ6s5zJ6AAXR6XD081GgbwFNKkN'
access_token_secret= 'R3QzGl2UFfYxcxaHjamT1e3vLVSR74i4qxcKjysEmzWIV'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the data_since date
search_words = "columbine -filter:retweets"
# date format as 2018-11-16
date_since = "2020-02-13"
# Collect tweets
tweets = tw.Cursor(api.search,
                   q=search_words,
                   lang="en",
                   since=date_since).items(100) # amt of tweets to return 

users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
print(users_locs)

tweet_text = pd.DataFrame(data=users_locs,   # creates table
                          columns=['user', "location"])
print(tweet_text)




