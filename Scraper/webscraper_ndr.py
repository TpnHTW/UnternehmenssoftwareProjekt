import requests

url_others = 'https://www.ndr.de/suche10.html?query=fleischersatz&sort_by=date&range=unlimited&results_per_page=50#'

import pandas as pd

# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:
page = requests.get(url_others).content

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, 'html.parser')

teasers = soup.find_all(class_='content')

# Print the number of elements found
print(f"Number of elements found: {len(teasers)}")
data = []

count = 0
# You can access the content of each element using a loop:
for teaser in teasers:
    # Find all 'a' tags within the teaser
    links = teaser.find_all('a')

    # Print the 'href' attribute of each 'a' tag
    for link in links:
        article_url = link['href']

        # Make a request to the article's URL
        article_page = requests.get(article_url)

        # Parse the HTML of the article page
        article_soup = BeautifulSoup(article_page.content, 'html.parser')
        # Find the title of the article
        title = article_soup.find('h2').text

        date = ""
        # Find the publishing date of the article
        if article_soup.select_one('[class="lastchanged"]') is not None:
            date = article_soup.select_one('[class="lastchanged"]').text
        elif article_soup.select_one('[itemprop="startDate"]') is not None:
            date = article_soup.select_one('[itemprop="startDate"]').text
        else:
            date = "notfound"

        # Find the text of the article
        textPart = article_soup.select('[id="page"]')
        article_text = ""
        for text in textPart:
            paragraphs = text.find_all('p')
            for p in paragraphs:
                article_text = article_text + p.text

        # article_text = textPart.find_all('p')
        # Print the title, date, and text of the article
        article_data = {
            'title': title,
            'date': date,
            'text': article_text
        }

        data.append(article_data)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)
df = df.drop_duplicates('title')
df = df.drop_duplicates('date')
df = df.reset_index(drop=True)
print(df)
# Print the DataFrame
# Save the DataFrame as a CSV file
df.to_csv('articles_ndr.csv', index=False)
