from rapidfuzz import fuzz
import pandas as pd
import time
# Load the data from the first file into a DataFrame
df1 = pd.read_excel('3000er.xlsx')

# Load the data from the second file into a DataFrame
df2 = pd.read_excel('UNIQUE6.xlsx')


start_time = time.time()

# Define a function to compare two strings and return a similarity score
def similarity(s1, s2):
    return fuzz.token_sort_ratio(str(s1), str(s2))


# Define a threshold similarity score
threshold = 80

# Create an empty DataFrame to store the duplicates and similar instances
duplicates = pd.DataFrame(columns=df1.columns)

# Loop through each row of the first DataFrame
for i, row1 in df1.iterrows():

    # Compare the current row to all rows in the second DataFrame
    for j, row2 in df2.iterrows():

        # Compare the fields (Name, Adresse, Ansprechperson, Email) using the rapidfuzz library
        sim1 = similarity(row1['Name'], row2['Name'])
        sim2 = similarity(row1['Adresse'], row2['Adresse'])
        sim3 = similarity(row1['Ansprechperson'], row2['Ansprechperson'])
        sim4 = similarity(row1['Email'], row2['Email'])

        # If the similarity score is above the threshold, the rows are considered duplicates or similar instances
        if sim1 >= threshold and sim2 >= threshold and sim3 >= threshold and sim4 >= threshold:
            duplicates = duplicates._append(row1, ignore_index=True)
            duplicates = duplicates._append(row2, ignore_index=True)

# Save the duplicates and similar instances to a new file
duplicates.to_csv('duplicates3000-80.csv', index=False)
duplicates.to_excel('duplicates3000-80.xlsx')

end_time = time.time()
timespent = end_time - start_time
timespent = timespent / 60
print(f"Das Script hat {timespent} Minuten Dgebraucht")