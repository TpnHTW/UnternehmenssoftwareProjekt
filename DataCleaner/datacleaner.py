import pandas as pd
import re

df = pd.read_csv('resulttoexplore.csv')
print(df.describe())

# Remove HTML tags and newline characters
df['text'] = df['text'].replace(r'<[^>]*>', '', regex=True).replace(r'\n', '', regex=True)
df['title'] = df['title'].replace(r'<[^>]*>', '', regex=True).replace(r'\n', '', regex=True)

# Remove punctuation
df['text'] = df['text'].replace(r'[^\w\s]', '', regex=True)
df['title'] = df['title'].replace(r'[^\w\s]', '', regex=True)

df = df.dropna().reset_index(drop=True)
df = df.drop_duplicates()

df.to_csv("cleaned_text.csv", index=False)
print(df)
