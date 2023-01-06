import requests

import pandas as pd
import numpy as np

from Levenshtein import distance
from sklearn.cluster import KMeans

# süddeutscheZeitung ist ein Fuchs mit dem Link zu den Seiten != 1
# Send the request with the POST method

# Set the URL of the protected page

# Send the request with the GET method

# Google Chrome - Menu - Weitere Tools - Entwicklertools
# Ctrl+Shift+C - Select section of interest
# Right click html code and copy XPath:

from bs4 import BeautifulSoup

# Open the HTML file
with open('htmlfaz.html') as f:
    # Read the contents of the file
    contents = f.read()

soup = BeautifulSoup(contents, 'html.parser')

teasers = soup.find_all(class_="single-document")

# Print the number of elements found
print(f"Number of elements found: {len(teasers)}")
data = []
for teaser in teasers:
    # Find the title of the article
    # Find the text of the article
    # Find the publishing date of the article
    contents = teaser.find(class_='articlemain__content')
    date = teaser.find(class_="docSource")
    title = teaser.find_next(class_="docTitle")
    article_text = teaser.find_next(class_="text")
    text = ""
    for article in article_text:
        text = text + article.text

    # Print the title, date, and text of the article
    article_data = {
        'title': title.text,
        'date': date.text,
        'text': text
    }
    data.append(article_data)
# You can access the content of each element using a loop:

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)
df = df.drop_duplicates('title')
df = df.drop_duplicates('text')

#Duplikate mittels veröffentlichungsdatum finden und löschen

# Test the function
print(df)
df = df.reset_index(drop=True)
# Print the DataFrame
# Save the DataFrame as a CSV file
df.to_csv('articles_faz.csv', index=False)
