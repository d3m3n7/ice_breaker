import os
import logging

import tweepy

logger = logging.getLogger("twitter")


def get_bearer_token() -> str:
    return os.environ["TWITTER_BEARER_TOKEN"]


def get_twitter_consumer_api_key() -> str:
    return os.environ["TWITTER_CONSUMER_API_KEY"]


def get_twitter_consumer_api_secret() -> str:
    return os.environ["TWITTER_CONSUMER_API_SECRET"]


def get_twitter_access_token() -> str:
    return os.environ["TWITTER_ACCESS_TOKEN"]


def get_twitter_access_token_secret() -> str:
    return os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

def get_api():
    auth = tweepy.OAuth1UserHandler(
        consumer_key=get_twitter_consumer_api_key(),
        consumer_secret=get_twitter_consumer_api_secret(),
        access_token=get_twitter_access_token(),
        access_token_secret=get_twitter_access_token_secret(),
    )
    return tweepy.API(auth)

# TODO: This function requires a subscription to the Twitter API.
#       The basic plan costs 100$ which is the cheapest that allows READING tweets.
#       The current subscription I have only allows POSTing tweets which renders it useless for data scrapping
def scrape_user_tweets(username, num_tweets=5):
    api = get_api()
    tweets = api.user_timeline(screen_name=username, count=num_tweets)
    print(tweets)
