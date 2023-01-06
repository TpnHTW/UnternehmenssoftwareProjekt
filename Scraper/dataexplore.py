import pandas as pd

# Read in the first CSV file
df1 = pd.read_csv("articles_ndr.csv", header=0)

# Read in the second CSV file
df2 = pd.read_csv("articles_ntv.csv", header=0)

# Read in the third CSV file
df3 = pd.read_csv("articles_sz.csv", header=0)

# Concatenate the dataframes horizontally
result = pd.concat([df1, df2, df3], axis=0, names=df1.columns.tolist())

# Save the result to a new CSV file
result.to_csv("/Users/philipnartschik/PycharmProjects/pythonProject2/DataExplore/resulttoexplore.csv", index=False)
