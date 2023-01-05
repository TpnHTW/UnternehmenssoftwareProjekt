import requests

url_others = 'https://www.lebensmittelzeitung.net/suche/?OK=1&i_q=fleischersatz&i_sortfl=pubdate&i_sortd=desc&currPage='

import pandas

url = url_others

# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:
page = requests.get(url_others+'1').content

page = page + requests.get(url_others+'2').content

page = page + requests.get(url_others+'3').content
print(page)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

