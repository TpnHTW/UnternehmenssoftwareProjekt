import pandas as pd
import re

df = pd.read_csv('resulttoexplore.csv')
print(df.describe())
df.info()