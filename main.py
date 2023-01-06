import requests

# süddeutscheZeitung ist ein Fuchs mit dem Link zu den Seiten != 1
urls = ['https://sz-magazin.sueddeutsche.de/essen-und-trinken/schmorgerichte-vegan-vegetarisch-fleischlos-umami-92193']
# 'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&all%5B%5D=time',
# 'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&time=2000-01-05T00%3A00%2F2020-08-15T23%3A59&startDate=05.01.2000&endDate=15.08.2020',
# 'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&time=2000-01-05T00%3A00%2F2020-08-15T23%3A59&startDate=05.01.2000&endDate=14.05.2019']

import pandas as pd

import requests

url = 'https://id.sueddeutsche.de/login'

# Set the credentials you want to send
payload = {
    'username': 'philipnartschik96@gmail.com',
    'password': '@S%&Jpbe7LiwzL_'
}

# Send the request with the POST method
login_response = requests.post(url, data=payload)

# Set the URL of the protected page

# Send the request with the GET method
page = ""

for url in urls:
    response = requests.get(url, cookies=login_response.cookies)
    # Check the response status code
    if response.status_code == 200:
        # If the status code is 200, the request was successful
        # You can now use the response.text to access the HTML of the page
        page = page + response.content.decode('utf-8')
    else:
        # If the status code is not 200, there was an error
        print('An error occurred:', response.status_code)

# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')

print(soup.find_all('p'))
