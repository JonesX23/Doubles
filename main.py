import csv
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

data = pd.read_csv("mitglieder.csv", on_bad_lines='skip', encoding="ISO-8859-1", sep=';', engine='python')
data.dropna(subset=['Name'], how='any', inplace=True)



data.dropna(subset=data.columns.difference(['Name']), how='all', inplace=True)
# print(data)
data['Name'] = df['Name'].str.strip()


# print(data.columns)


duplicates = data[data.duplicated()]
# Loop through each duplicate row and print the selected columns
# for index, row in duplicates.iterrows():
#     print(f"Duplicate {index + 1}:")
#     print(row.loc[['Name']])

data = data.drop_duplicates()
#
# similarity_threshold = 0.1 # Set the similarity threshold here
# similarity_cols = ['Name']  # Set the columns to use for similarity comparison here
# similarity_group = data2.groupby(similarity_cols).size().reset_index(name='count')
# possible_duplicates = similarity_group[similarity_group['count'] > 1]


# similarity_threshold = 0.1
# similarity_cols = ['Name', 'PLZ', 'Telefon 1']
# similarity_group = data.groupby(similarity_cols).size().reset_index(name='count')
# possible_duplicates = similarity_group[similarity_group['count'] > 1]
#
# # Create a new DataFrame to store the rows with the most complete information
# filtered_data = pd.DataFrame(columns=data.columns)
#
# # Iterate through each group of possible duplicates
# for _, group in possible_duplicates.groupby(similarity_cols):
#     # Create a list to store the completeness score for each row in the group
#     completeness_scores = []
#     for index, row in group.iterrows():
#         # Calculate the completeness score for the row
#         completeness_score = 1 - np.sum(row.isnull()) / len(row)
#         completeness_scores.append(completeness_score)
#     # Find the index of the row with the highest completeness score
#     max_index = completeness_scores.index(max(completeness_scores))
#     # Add the row with the highest completeness score to the new DataFrame
#     filtered_data = filtered_data._append(group.iloc[max_index], ignore_index=True)

# define a similarity threshold (e.g., 80%)
threshold = 80

# compare each row to the others and remove duplicates based on similarity score
to_remove = set()
for i, row1 in data.iterrows():
    for j, row2 in data.iterrows():
        if i == j:
            continue
        similarity = fuzz.token_set_ratio(row1, row2)
        if similarity >= threshold:
            to_remove.add(j)
print("REMOVE BY FUZZYWUZZY")
print(to_remove)
#df = df.drop(to_remove)



# Print the new DataFrame
#print("FILTERED DATA")
#print(filtered_data)

##Print the possible duplicates
# print("ALLE DUPLIKATE")
# print(data.duplicated)
#print("MÖGLICHE DUPLIKATE NACH ÄHNLICHKEIT")
#print(possible_duplicates)
# data2.to_csv('Mitglieder-bereinigt.csv')
# data2.to_excel('Mitglieder.bereinigt.xlsx')
# filtered_data.to_excel('DuplettenMultipleAnsprechpartner.xlsx')
