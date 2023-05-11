from fuzzywuzzy import fuzz
import pandas as pd
import time
# Load the data into a DataFrame

start_time = time.time()

df = pd.read_csv("mitglieder.csv", on_bad_lines='skip', encoding="ISO-8859-1", sep=';', engine='python')
# Remove exact duplicates
# Load the data into a DataFrame

# Remove exact duplicates
df.drop_duplicates(inplace=True)


# Define a function to compare two strings and return a similarity score
def similarity(s1, s2):
    return fuzz.token_sort_ratio(str(s1), str(s2))


# Define a threshold similarity score
threshold = 90
name_threshold = 85

# Create an empty DataFrame to store the unique entries
unique = pd.DataFrame(columns=df.columns)

# Create a new DataFrame to store the non-unique entries
non_unique = pd.DataFrame(columns=df.columns)

# Loop through each row of the DataFrame
for i, row1 in df.iterrows():

    # Assume the current row is unique
    is_unique = True

    # Compare the current row to all previous rows
    for j, row2 in unique.iterrows():

        # Compare the fields (Name, Adresse, Ansprechperson, Email) using the rapidfuzz library
        sim1 = similarity(row1['Name'], row2['Name'])
        sim2 = similarity(row1['Adresse'], row2['Adresse'])
        sim3 = similarity(row1['Ansprechperson'], row2['Ansprechperson'])
        sim4 = similarity(row1['Email 1'], row2['Email 1'])
        sim5 = similarity(row1['Ort'], row2['Ort'])


        # If the similarity score is above the threshold, the rows are considered duplicates
        if sim1 >= name_threshold and sim2 >= threshold and sim3 >= threshold and sim4 >= threshold and sim5>= threshold:
            is_unique = False
            break

    # If the row is unique, add it to the unique DataFrame; otherwise, add it to the non_unique DataFrame
    if is_unique:
        unique = unique._append(row1, ignore_index=True)
    else:
        non_unique = non_unique._append(row1, ignore_index=True)

# The unique DataFrame contains only the unique entries
unique.to_csv('UNIQUE5.csv')
unique.to_excel('UNIQUE-EXCEL5.xlsx')
non_unique.to_excel('removed3.xlsx')


end_time = time.time()
timespent = end_time - start_time
timespent = timespent / 60
print(f"Das Script hat {timespent} Minuten gebraucht")
