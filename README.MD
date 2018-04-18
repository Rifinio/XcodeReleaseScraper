### XCode Release notifier
This script scrapes the apple release page and checks if there is a new version available.
It uses webhooks to send back a message into the given slack channels.

#### Setup using virtualevn

1) In the project home directory, start a virtualevn:
`virtualenv venv` 
2) activate virtual env
`source venv/bin/activate`
3) install dependencies
```
pip install BeautifulSoup4
pip install requests
```
#### Run
To run the script :
```
python scrapy.py
```