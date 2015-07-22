""" Workhorse of the entire f'n thing. """
# begin imports, so your tears will dry upwards
import time
import tweepy
import logging
import random
import datetime

# constants - should look into making a settings.py
API_KEY = '3ay665fsUUBiOJK6xca8b3ile'
API_SECRET = '8uLWktHANOxU5gcyimL9JE6Ql765DZFBNX6vlBOmG6S643QBBz'
ACCESS_TOKEN = '3385189491-pVnK0Y16EgQUDIYiX4pka0MfFfqgokYl2l4QZvN'
ACCESS_SECRET = 'aY0vilDkj07vKjXZTpp6G1NRi8DLvllVd2HmowcE0zncQ'

log = logging.getLogger()

def connect():
    """Initiate connection with twitter."""

    # log.info('CONSUMER_KEY %s', API_KEY)        ----
    # log.info('CONSUMER_SECRET %s', API_SECRET)     |--- un-comment if you'd like,
    # log.info('ACCESS_KEY %s', ACCESS_TOKEN)        |    just for debugging
    # log.info('ACCESS_SECRET %s', ACCESS_SECRET) ----

    # connect to twitter
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    return api

def send_tweet(line, api_con):
    """ Very simply sends a tweet given the line as an argument. """

    if line != "":
        api_con.update_status(status=line)

def choose_line():
    """ Chooses a line from a dictionary of Godspeed You! Black Emperor songs. """

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
    r_int = random.randint(0, num_of_lines)

    # get the line
    pointer = 0
    for line in file_list:
        if pointer == r_int:
            if line[0] != '#':
                log.info('pointer = %s, rInt = %s, num_of_lines = %s ', pointer, r_int, num_of_lines) # debug only
                return line
        # just to be safe or something?
        elif pointer > num_of_lines:
            line = ""
            return line
        else:
            pointer += 1

def main():
    """ Main function. """
    logging.basicConfig(filename='./logs/gybote.log', level=logging.INFO)
    log.info('Starting jtb...')

    api_con = connect()

    # work on clean shutdown to get rid of this while True
    while True:
        line = ""

        log.info('Choosing word to tweet...')
        line = choose_line()

        log.info('Sending tweet...')
        send_tweet(line, api_con)
        log.info('Tweet sent with the line: %s', line)

        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        log.info('------------------------------%s------------------------------------', date_time)

        # sleep for 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    main()