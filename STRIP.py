import pandas as pd

df = pd.read_excel('Mitglieder-bereinigt-stripped-phone.xlsx')
#df = pd.read_excel('Mitglieder-bereinigt1505.xlsx')


df.dropna(subset=['Name'], inplace=True)
df['Name'] = df['Name'].str.strip()
df['PLZ'] = df['PLZ'].str.strip()
df['Ort'] = df['Ort'].str.strip()
df['Email 1'] = df['Email 1'].str.strip()
df['Name'] = df['Name'].str.strip()

df['Ansprechperson'] = df['Ansprechperson'].str.strip()
df.to_excel('Mitglieder-bereinigt-stripped-stripped-phone.xlsx')
#df.to_csv("Unique6.csv")