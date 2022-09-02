import pandas as pd

df1 = pd.read_excel('Web Scrapping_Sample Records.xlsx')

df2 = pd.read_csv("martindale.csv") 

df = pd.concat([df1, df2])
df.to_csv("combine_data.csv", index=False)