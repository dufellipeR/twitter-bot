import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

# user = api.get_user('DuuuuFR')
# print(user.screen_name)
# print(user.followers_count)

# api.update_status(status="Hello World")

tweet_list = api.favorites(screen_name="DuuuuFR")
# for tweet in tweet_list:
#     print(tweet.text, tweet.user.name, tweet.user.location, tweet.id)

# tweet_id = 1214748531195551750

# api.retweet(tweet_id)

for tweet in tweet_list:
    try:
        api.retweet(tweet.id)
    except tweepy.TweepError as e:
        print(e)
        