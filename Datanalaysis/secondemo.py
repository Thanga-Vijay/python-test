import pandas as pd

df = pd.read_csv('D:\\userdetails\\Python_class\\Datanalaysis\\dirtydata.csv')

df['Date'].fillna(135,inplace=True)

new_df = df.dropna(inplace=True)

print(df)
