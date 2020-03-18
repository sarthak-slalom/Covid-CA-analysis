import json
import tweepy
import re
from collections import Counter
import pandas as pd


# define twitter api keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

# authenticate twitter api
auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# search term
search_term = "social distance"

# search twitter via tweepy api search
tweets = tweepy.Cursor(api.search,
                   q=search_term,
                   lang="en",
                   wait_on_rate_limit = True).items()

# get the created date and count how many tweets for each date
created_dates = [tweet.created_at.date() for tweet in tweets]
d = Counter(created_dates)

# create dictionary for each created date
created_date_dict = {}
for date in created_dates:
    created_date_dict[str(date)] = d[date]

# create pandas dataframe
date_counts = pd.DataFrame.from_dict(created_date_dict, orient = 'index')
date_counts.columns = ['number of mentions']

# write to csv with date and number of mentions
date_counts.to_csv("date_counts.csv")

