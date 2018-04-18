# import libraries
import urllib2
from bs4 import BeautifulSoup

# Variables
url = 'https://developer.apple.com/news/releases/'
word_to_look_for = 'XCode'
latest_release_version = '9.3'

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

if new_release_version > float(latest_release_version):
	print("Found it !", last_news_release)
else: 
	print("No new releases for " + word_to_look_for)