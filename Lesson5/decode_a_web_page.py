# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times

import requests
from bs4 import BeautifulSoup

print("This program will take New York Times html and print out all article titles. \n")

url = "https://www.nytimes.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

for story_heading in soup.find_all(class_='story-heading'):
    if story_heading.a:
        print(story_heading.a.text.replace('\n', ' ').strip() + '\n')
    else:
        print(story_heading.contents[0].strip() + '\n')