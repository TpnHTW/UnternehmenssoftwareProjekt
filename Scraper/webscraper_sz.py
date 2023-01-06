import requests

import pandas as pd
# süddeutscheZeitung ist ein Fuchs mit dem Link zu den Seiten != 1
urls = [
    'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&all%5B%5D=time',
    'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&time=2000-01-05T00%3A00%2F2020-08-15T23%3A59&startDate=05.01.2000&endDate=15.08.2020',
    'https://www.sueddeutsche.de/news?search=Fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&time=2000-01-05T00%3A00%2F2020-08-15T23%3A59&startDate=05.01.2000&endDate=14.05.2019',
    'https://www.sueddeutsche.de/news?search=fleischersatz&sort=date&all%5B%5D=dep&all%5B%5D=typ&all%5B%5D=sys&time=2000-01-06T00%3A00%2F2014-04-02T23%3A59&startDate=06.01.2000&endDate=02.04.2014']


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

teasers = soup.find_all(class_="entrylist__link")

# Print the number of elements found
print(f"Number of elements found: {len(teasers)}")
data = []

for teaser in teasers:
    # Find all 'a' tags within the teaser
    article_url = teaser['href']
    # Print the 'href' attribute of each 'a' tag

    # Make a request to the article's URL
    article_page = requests.get(article_url)

    # Parse the HTML of the article page
    article_soup = BeautifulSoup(article_page.content, 'html.parser')

    # Find the title of the article
    if article_soup.find(class_="video-article-wrapper") is not None:
        print('video')
    else:
        # Find the text of the article
        # Find the publishing date of the article
        contents = article_soup.find(class_='articlemain__content')
        date = article_soup.find(class_="list__item list__item--horizontal metabar__item")
        if contents is None:
            contents = article_soup.select_one('[itemprop="articleBody"]')
            date = article_soup.select_one('[class="css-1r5gb7q"]')
            article_text = contents.find_all('p')
            text = ""
            for article in article_text:
                text = text + article.text

            title = ""
            # Find the title of the article
            if article_soup.find(
                    class_="headline headline--h1 articleheader__headline articleheader__headline--h1 flipboard-title") is not None:
                title = article_soup.find(
                    class_="headline headline--h1 articleheader__headline articleheader__headline--h1 flipboard-title").text
            elif article_soup.find(class_="css-1bhnxuf") is not None:
                title = article_soup.find(class_="css-1bhnxuf").text
            # Print the title, date, and text of the article
            article_data = {
                'title': title,
                'date': date.text,
                'text': text
            }
            data.append(article_data)
# You can access the content of each element using a loop:

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)
df = df.drop_duplicates('title')
df = df.reset_index(drop=True)
print(df)
# Print the DataFrame
# Save the DataFrame as a CSV file
df.to_csv('articles_sz.csv', index=False)
