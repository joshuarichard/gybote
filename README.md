# gybote
A twitter bot that tweets Godspeed You! Black Emperor lyrics.

### Dependencies
The only external dependency that gybote requires is Tweepy, one of the many python-twitter APIs. Tweepy was chosen because well, it's easy.

You can read more about tweepy here: http://docs.tweepy.org/en/v3.2.0/

To install:
```shell
$ pip install tweepy
```

In addition to tweepy there is also the possibility that you require one more additional dependency. If you are running into the problem where urllib3 cannot establish a secure connection and you are receiving the below error then you need to install requests.
```
/usr/local/lib/python2.7/dist-packages/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
```

Requests is a python http library that essentially auto-injects itself into your http requests, doing all of the heavy lifting for you.

You can read more about requests here: http://docs.python-requests.org/en/latest/

To install:
```shell
$ pip install requests[security]
```

### Configuration
The only changes required for gybote to run are the four credentials required by Twitter. 

These are defined at the top of gybote.py as API_KEY, API_SECRET, ACCESS_TOKEN, and ACCESS_SECRET. They can be found by going to the settings page for your app and clicking on "Keys and Access Tokens".

### Running

cd into the project's root directory and run:
```shell
$ python gybote.py
```
### Dictionary
gybote uses a dictionary of all the Godspeed lyrics I could find or transcribe myself. It should not be considered a complete dictionary. Given this, I suggest not to use gybote in production environments quite yet. The dictionary can be found in the /dict directory as gybe-lyrics.txt.

The character '#' is used to denote a comment. The code that accounts for this can be found in gybote.py, however in gybote.py it might look slightly different.

Feel free to add your own dictionaries for use with gybote.py.

```python
# get the line
pointer = 0
for line in file_list:
    if pointer == r_int:
        if line[0] != '#':
            return line
    else:
        pointer += 1
```

### File Structure

```
├── dict
|   └── gybe-lyrics.txt
├── gybote
|   └── gybote.py
├── logs
|   └── gybote.log
├── README.md
└── LICENSE
```
