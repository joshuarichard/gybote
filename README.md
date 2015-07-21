# gybote
A twitter bot that tweets Godspeed You! Black Emperor lyrics.

### Dependencies
The only external dependency that gybote requires is Tweepy, one of the many python-twitter APIs. Tweepy was chosen because well, it's easy.

You can find it here: https://github.com/tweepy/tweepy

To install:
```shell
$ pip install tweepy
```
    
### Configuration
The only changes required for gybote to run are the four credentials required by Twitter. 

These are defined at the top of gybote.py as API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_SECRET. They can be found by going to the settings page for you app and clicking on "Keys and Access Tokens".

### Running
gybote uses a dictionary of all the Godspeed songs I could find or transcribe myself. It should not be considered a complete dictionary. Given this, we suggest not to use gybote in production environments quite yet. The dictionary can be found at '/dict/gybe-lyrics.txt'.

cd into the project's root directory and run:
```shell
$ python gybote.py
```

### File Structure

```
├── dict
|   └── gybe-lyrics.txt
├── logs (created at runtime)
|   └── gybote.log
├── gybote.py
├── README.md
└── LICENSE
```
