import pandas as pd
import re

df = pd.read_csv('resulttoexplore.csv')
print(df.describe())

# Remove HTML tags and newline characters
df['text'] = df['text'].replace(r'<[^>]*>', '', regex=True).replace(r'\n', '', regex=True)

# Remove punctuation
df['text'] = df['text'].replace(r'[^\w\s]', '', regex=True)
df.info()