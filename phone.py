import pandas as pd
import re

df = pd.read_excel('Mitglieder-bereinigt-stripped.xlsx')
df['Telefon 1'] = df['Telefon 1'].apply(lambda x: re.sub(r'\D', '', str(x)))

# Save the updated DataFrame to a new file
df.to_excel('Mitglieder-bereinigt-stripped-phone.xlsx', index=False)