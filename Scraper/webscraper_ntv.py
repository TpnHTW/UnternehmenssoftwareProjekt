import requests

url_others = 'https://www.n-tv.de/suche/?q=fleischersatz&at=all&page='

import pandas as pd

# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:
page = requests.get(url_others + '1').content
page = page + requests.get(url_others + '2').content
page = page + requests.get(url_others + '3').content
page = page + requests.get(url_others + '4').content
page = page + requests.get(url_others + '5').content
page = page + requests.get(url_others + '6').content

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')

teasers = soup.find_all(class_='teaser teaser--inline')

# Print the number of elements found
print(f"Number of elements found: {len(teasers)}")
data = []
# You can access the content of each element using a loop:
ntv_urls = []
for teaser in teasers:
    # Find all 'a' tags within the teaser
    links = teaser.find_all('a')

    # Print the 'href' attribute of each 'a' tag
    for link in links:
        ntv_urls.append(link['href'])
        article_url = link['href']

        # Make a request to the article's URL
        article_page = requests.get(article_url)

        # Parse the HTML of the article page
        article_soup = BeautifulSoup(article_page.content, 'html.parser')

        # Find the title of the article
        title = article_soup.find(class_='article__headline').text

        # Find the publishing date of the article

        date = article_soup.find(class_='article__date')
        # Find the text of the article
        article_text = article_soup.find_all('p')
        text = ""
        for article in article_text:
            text = text + article.text

        # Print the title, date, and text of the article
        if date is not None:
            article_data = {
                'title': title,
                'date': date.text,
                'text': text
            }
            data.append(article_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)
df = df.drop_duplicates('title')
df = df.reset_index(drop=True)
print(df)
# Print the DataFrame
# Save the DataFrame as a CSV file
df.to_csv('articles_ntv.csv', index=False)


