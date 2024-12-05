#python email scraping for project 


import requests
from bs4 import BeautifulSoup
url="https://worldpress.com.pk/technology-news/pakistan-email-list/"
response = requests.get(url)
soup = BeautifulSoup(response.content,\
                     'html.parser')
emails = []
for link in soup.find_all('a'):
    if 'mailto:' in link.get('href'):
        emails.append(link.get('href').\
                      split(' : ')[0])
print(emails)
