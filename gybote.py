""" Workhorse of the entire f'n thing. """
# begin imports, so your tears will dry upwards
import time
import tweepy
import logging
import random
import datetime

# constants - should make these env vars if deploying to BM
API_KEY = ''
API_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

log = logging.getLogger()

def send_tweet(line):
    """ Sends a tweet given the line as an argument. """

    log.info('Connecting to twitter with credentials:')
    log.info('CONSUMER_KEY %s', API_KEY)
    log.info('CONSUMER_SECRET %s', API_SECRET)
    log.info('ACCESS_KEY %s', ACCESS_TOKEN)
    log.info('ACCESS_SECRET %s', ACCESS_SECRET)

    # connect to twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    log.info('Connected to twitter, now sending tweet...')

    # send tweet
    api.update_status(status=line)

def choose_line():
    """ Chooses a line from a dictionary of Godspeed You! Black Emperor songs. """

    line = ""

    # load dictionary
    file_name = open('./dict/gybe-lyrics.txt', 'r')
    file_list = file_name.readlines()
    file_name.close()

    # find out how many lines the are in the dictionary
    num_of_lines = 0
    for line in file_list:
        num_of_lines += 1

    # subtract 1 because I don't like to fuck w/ indices
    num_of_lines = num_of_lines - 1

    # pick a random line
    r_int = random.randint(0, num_of_lines - 1)

    # get the line
    pointer = 0
    for line in file_list:
        if pointer == r_int:
            if line[0] != '#':
                log.info('pointer = %s, rInt = %s, num_of_lines = %s ', pointer, r_int, num_of_lines) # debug only
                return line
        # just to be safe or something?
        elif pointer > num_of_lines:
            return ""
        else:
            pointer += 1

def main():
    """ Main. """
    logging.basicConfig(filename='./logs/gybote.log', level=logging.INFO)

    log.info('Starting jtb...')

    # work on clean shutdown
    while True:
        log.info('Choosing word to tweet...')
        line = choose_line()

        log.info('Sending tweet...')
        send_tweet(line)

        log.info('Tweet sent with the line: %s', line)
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        log.info('------------------------------%s------------------------------------', date_time)

        # sleep for 10 minutes
        time.sleep(600)

if __name__ == "__main__":
    main()
