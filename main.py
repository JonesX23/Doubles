import csv
import pandas as pd

data = pd.read_csv("mitglieder.csv", on_bad_lines='skip', encoding="ISO-8859-1", sep=';', engine='python')
data.dropna(subset=['Name'], how='any', inplace=True)



data.dropna(subset=data.columns.difference(['Name']), how='all', inplace=True)
# print(data)


# print(data.columns)


duplicates = data[data.duplicated()]
# Loop through each duplicate row and print the selected columns
for index, row in duplicates.iterrows():
    print(f"Duplicate {index + 1}:")
    print(row.loc[['Name']])

data2 = data.drop_duplicates()

similarity_threshold = 0.5 # Set the similarity threshold here
similarity_cols = ['Name', 'Adresse ', 'Ort ',
                   'Ansprechperson ']  # Set the columns to use for similarity comparison here
similarity_group = data2.groupby(similarity_cols).size().reset_index(name='count')
possible_duplicates = similarity_group[similarity_group['count'] > 1]

# Print the possible duplicates
print("ALLE DUPLIKATE")
print(data.duplicated)
print("MÖGLICHE DUPLIKATE NACH ÄHNLICHKEIT")
print(possible_duplicates)
# data2.to_csv('Mitglieder-bereinigt.csv')
# data2.to_excel('Mitglieder.bereinigt.xlsx')

print(data2)