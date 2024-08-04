import pandas as pd

file_path = 'crop_yield.csv'
df = pd.read_csv(file_path)

print(df.head())

print(df.info())

print(df.describe())