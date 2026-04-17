import pandas as pd
import re
import csv
#df = pd.read_csv('alumni_anonymized.csv', index_col='Name')
def fill_year(year_str):
    match= re.search(r'\d{2,4}', year_str)
    if not match:
        return None
    year = match.group()
    if len(year) == 2:
        if int(year) < 82:
            year = '19' + year
        else:
            year = '18' + year
    return year

 
    

with open('alumni_anonymized.csv') as records:
    reader = csv.reader(records)
    entries = [] #this will store the rows in dictionary form
    next(reader)  #skip header
    count = 0
    for row in reader:
        if row[1]:
            new_row = dict()
            if count < 6:
                print(row)
                print(row[0])
            new_row['Exit_Year'] = fill_year(row[1])
            new_row['Last_Name'] = row[0]
            new_row['Id_Number'] = row[3]
            entries.append(new_row)
            count+=1


with open('alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file,fieldnames=['Last_Name','Exit_Year','Id_Number'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)

with open('alumni_clean.csv', 'r') as new_file:  # separate block to read
    file = csv.reader(new_file)
    next(file)
    count = 0
    for row in file:
        if count < 50:
            print(row)  # also changed new_row to row here
            count += 1

