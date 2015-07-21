# gybote
A twitter bot that tweets Godspeed You! Black Emperor lyrics.

## Dependencies
The only external dependency that gybote requires is one of the many python-twitter APIs. This bot uses Tweepy.

You can find it here: https://github.com/tweepy/tweepy

To install:
'''$ pip install tweepy'''
    
### Configuration
The only changes required for gybote to run are the four credentials required by Twitter. 

These are defined at the top of gybote.py as API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_SECRET. They can be found by going to the settings page for you app and clicking on "Keys and Access Tokens".

#### Compilation
cd into the project's root directory and run:
'''$ python gybote.py'''
