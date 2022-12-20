import requests

url_others = 'https://www.washingtonpost.com/search/?query=beyond+meat&facets=%7B%22time%22%3A%22all%22%2C%22sort%22%3A' \
      '%22relevancy%22%2C%22section%22%3A%5B%5D%2C%22author%22%3A%5B%5D%7D'

import pandas

df1 = pandas.read_csv(url_others, sep='|')

url =
# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:
page = requests.get(url).content
print(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

#<article class="single-result mt-sm pb-sm"
#<a href = "https://www.washingtonpost.com/food/2020/11/10/mcdonalds-mcplant-sandwich/" class ="font-md font--magazine-headline font-bold mb-sm black" >

https://www.washingtonpost.com/search/?query=beyond+meat&facets=%7B%22time%22%3A%22all%22%2C%22sort%22%3A%22relevancy%22%2C%22section%22%3A%5B%5D%2C%22author%22%3A%5B%5D%7D
https://www.washingtonpost.com/search/?query=beyond+meat&facets=%7B%22time%22%3A%22all%22%2C%22sort%22%3A%22relevancy%22%2C%22section%22%3A%5B%5D%2C%22author%22%3A%5B%5D%7D