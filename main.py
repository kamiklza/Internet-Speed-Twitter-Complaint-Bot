from selenium import webdriver
from twitterbot import InternetSpeedTwitterBot
import os


PROMISED_DOWN = 1000
PROMISED_UP = 1000
desktop_driver_path = "C:/Users/user/PycharmProjects/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

twitter_bot = InternetSpeedTwitterBot(PROMISED_DOWN, PROMISED_UP)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)