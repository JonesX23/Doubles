import pandas as pd


df = pd.read_csv("UNIQUE5.csv", on_bad_lines='skip', encoding="ISO-8859-1", sep=',', engine='python')

df.dropna(subset=['Name'], inplace=True)
df['Name'] = df['Name'].str.strip()
#df.to_excel("UNIQUE6.xlsx")
df.to_csv("Unique6.csv")