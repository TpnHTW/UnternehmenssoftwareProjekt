import requests
import beautifulsoup
URL = 'https://www.washingtonpost.com/search/?query=beyond+meat&facets=%7B%22time%22%3A%22all%22%2C%22sort%22%3A' \
      '%22relevancy%22%2C%22section%22%3A%5B%5D%2C%22author%22%3A%5B%5D%7D'

page = requests.get(URL)
soup =
print(page.text)
