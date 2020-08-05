import tweepy
import time

api_key = 'your api_key goes here'   # keep the quotations
api_secret_key = 'your api_secret_key goes here'
access_token = 'your access_token goes here'
access_token_secret = 'your access_token_secret goes here'

def OAuth():
	try:
		auth = tweepy.OAuthHandler(api_key, api_secret_key)
		auth.set_access_token(access_token, access_token_secret)
		return auth
	except Exception as e:
		return None

oauth = OAuth()
api = tweepy.API(oauth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def tweet():
	api.update_status('your tweet goes here {}'.format(time.ctime())) # Your tweet cannot exceed 256 characters

while True:
	tweet()
	time.sleep(60) # After every 60 seconds the tweet is posted with a different time stamp
