""" gybote, a twitter bot."""

# begin imports, so our tears will dry upwards
import time
import tweepy
import logging
import random
import datetime
from config import config

API_KEY = config["api_key"]
API_SECRET = config["api_secret"]
ACCESS_TOKEN = config["access_token"]
ACCESS_SECRET = config["access_secret"]

COMMENT_CHAR = config["comment_char"]
DICTIONARY_PATH = config["dictionary_path"]
SLEEP_FOR = int(config["sleep_for"])

log = logging.getLogger()

def connect():
    """Initiate connection with twitter."""

    # connect to twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api

def send_tweet(line, api_con):
    """ 
    Very simply sends a tweet given the line as an argument. 
    
    line - the line to tweet
    api_con - instance of the api to use
    """

    if line != "":
        try:
            api_con.update_status(status=line)
        except tweepy.TweepError:
            log.info('Caught tweepy error, trying again.')

def choose_line():
    """ Chooses a line from a dictionary of Godspeed You! Black Emperor songs. """

    file_name = open(DICTIONARY_PATH, 'r')
    file_list = file_name.readlines()
    file_name.close()

    num_of_lines = 0
    for line in file_list:
        num_of_lines += 1

    # subtract 1 because I don't like to fuck w/ indices
    num_of_lines = num_of_lines - 1

    r_int = random.randint(0, num_of_lines)

    pointer = 0
    for line in file_list:
        if pointer == r_int:
            if line[0] != COMMENT_CHAR:
                log.info('pointer = %s, rInt = %s, num_of_lines = %s ', pointer, r_int, num_of_lines)
                return line
        # just to be safe or something?
        elif pointer > num_of_lines:
            line = ""
            return line
        else:
            pointer += 1

def iteration():
    """Manages the process of sending one tweet."""

    log.info('Connecting to twitter.')
    api_con = connect()
    line = ""

    log.info('Choosing word to tweet.')
    line = choose_line()

    log.info('Sending tweet.')
    send_tweet(line, api_con)
    log.info('Tweet sent with the line: %s', line)

    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    log.info('----------------------------------------------------------------')
    log.info('------------------------%s------------------------', date_time)
    log.info('----------------------------------------------------------------')

    # sleep for 5 minutes
    time.sleep(SLEEP_FOR)

def main():
    """ Main function. """

    logging.basicConfig(filename='./logs/gybote.log', level=logging.INFO)
    log.info('Starting.')

    while True:
        iteration()
       

if __name__ == "__main__":
    main()
