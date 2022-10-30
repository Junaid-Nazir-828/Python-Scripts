import tweepy

TWITTER_CONSUMER_KEY= ""
TWITTER_CONSUMER_SECRET= ""
TWITTER_ACCESS_TOKEN= ""
TWITTER_ACCESS_SECRET= ""

auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY,TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

def post_tweet(text):    
    api.update_status(text)

post_tweet('This is a test tweet')

