import pandas as pd

#df = pd.read_csv("D:\\userdetails\\Python_class\\Datanalaysis\\demo.csv",encoding='utf-8')

df = pd.read_csv('D:\\Python_class\\Datanalaysis\\acc3.csv',) #, encoding='ISO-8859-1')

# print(df.head(10))

print(df.describe(include='all'))

print(df.info())

# count_row = df.shape[0]

# print("Count of rows :",count_row)

# df = pd.DataFrame(df)

# df.to_csv('D:\\userdetails\\Python_class\\Datanalaysis\\acc4.sql')
