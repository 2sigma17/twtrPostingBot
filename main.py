from twython import Twython, Twython Error
import configparser
import time

config = configparser.ConfigParser()

twtr = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
