import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import nltk
from nltk.corpus import stopwords
from textblob_de import TextBlobDE as TextBlob #2

df = pd.read_csv('cleaned_text.csv')

#Vortrainiertes SentimentModel gegen eigenes SentimentModel

holetext = ""
# Read in a text file
for part in df['text']:
    holetext = holetext + part
# Generate a wordcloud
wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color='salmon', colormap='Pastel1',
                      collocations=False, stopwords=stopwords.words('german')).generate_from_text(holetext)

# Display the wordcloud
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

df = pd.read_csv('cleaned_text.csv', sep=',')
text = df['text']

sentiment = []
sentiment_temp = []
result = []

for elem in text:
    blob = TextBlob(elem)
    for sentence in blob.sentences:
        sentiment_temp.append(sentence.sentiment.polarity)
    sentiment = (sentiment_temp)
    result.append(sentiment)

df['Sentiment'] = result
df.to_csv("./new_file_name.csv", sep=',', index=False)
