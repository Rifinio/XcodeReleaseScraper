# import libraries
import urllib2
from bs4 import BeautifulSoup
import os
import requests
import json

# Variables
url = 'https://developer.apple.com/news/releases/'
word_to_look_for = os.getenv('APPLE_KEYWORD', 'XCode')
latest_release_version = os.getenv('APPLE_VERSION', '9.3') 
channels = os.getenv('CHANNELS', 'slack-cahnnel-name').split(',') 
WEBHOOK_URL = os.getenv('WEBHOOK_URL') #use your own webhook url, in this case it's using slack

# Load the page
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# Get a list of new releases
news_boxes = soup.findAll('a', attrs={'class': 'article-title'})

# Loop through the news and append titles to a list
news_titles = []
for box in news_boxes:
	news = box.text.strip()
	news_titles.append(news)

# Find the latest xcode in the list of releases
last_news_release = ''
for title in news_titles:
	if word_to_look_for.upper() in title.upper():
		last_news_release = title
		break

# Check if a new release is out
release_data_split = last_news_release.split()
new_release_version = 0

if len(release_data_split) > 0:
	new_release_version = float(release_data_split[1])

message = ''
if new_release_version > float(latest_release_version):
	message = 'A new '+ word_to_look_for +' release is out :rocket:' + '\n:pizza_party: '+last_news_release + ' :pizza_party: \nFind out more here ' + url
	for channel in channels:
		response = requests.post(WEBHOOK_URL, data=json.dumps({"text" : message, "channel": "#"+ channel}), headers={'Content-Type': 'application/json'})
		print (response.text)
else:
	message = "No new releases for " + word_to_look_for

print(message)
