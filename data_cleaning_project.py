import pandas as pd
import re
import csv


def filter_exit_year(year_str):
    if not year_str:
        return None
    year = int(year_str)
    if year < 1880 or year > 1984:
        return None
    return year_str

def filter_birth_year(year_str):
    if not year_str:
        return None
    year = int(year_str)
    if year < 1857 or year > 1980:
        return None
    return year_str

def fill_year(year_str):
    match = re.search(r'\d{2,4}', year_str)
    if not match:
        return None
    year = match.group()
    if len(year) == 2:
        if int(year) < 82:
            year = '19' + year
        else:
            year = '18' + year
    return year

def clean_dob(dob_str):
    # returns None for empty data
    if not dob_str or not dob_str.strip():
        return None
    
    # remove labels like 'Born:' 'DOB' and anything after 'Died:'
    dob_str = re.sub(r'Died:.*', '', dob_str, flags=re.IGNORECASE)
    dob_str = re.sub(r'(Born:|DOB)', '', dob_str, flags=re.IGNORECASE)
    dob_str = dob_str.strip() # remove any potential whitespace
    
    # handle '28-Aug-30' style dates
    month_map = {
        'jan':'01','feb':'02','mar':'03','apr':'04',
        'may':'05','jun':'06','jul':'07','aug':'08',
        'sep':'09','oct':'10','nov':'11','dec':'12'
    }
    text_month = re.search(r'(\d{1,2})-([A-Za-z]{3})-(\d{2,4})', dob_str)
    if text_month:
        day = text_month.group(1).zfill(2)
        month = month_map[text_month.group(2).lower()]
        year = text_month.group(3)
        if len(year) == 2:
            year = '19' + year if int(year) < 82 else '18' + year
        return f'{year}' # originally had this function set up to return month, day, year but just changed the return value  to year
    
    # handle standard dates like '2/2/1929' or '04/18/1873'
    standard = re.search(r'(\d{1,2})[/\-](\d{1,2})[/\-](\d{2,4})', dob_str)
    if standard:
        month = standard.group(1).zfill(2) # zfill takes single digit months and puts a zero in front to maintain [2]/[2]/[4] western formatting
        day = standard.group(2).zfill(2)
        year = standard.group(3)
        if len(year) == 2:
            year = '19' + year if int(year) < 82 else '18' + year
        return f'{year}' # same deal here, just returned the year
    
    # handle hard cases like 'May 1947'
    month_year = re.search(r'([A-Za-z]+)\s+(\d{4})', dob_str)
    if month_year:
        return month_year.group(2)
    
    # handle only years, like Abbatiello's '1928'
    year = re.search(r'(\d{4})', dob_str)
    if year:
        return year.group(1) # technically dont need to use group here, but whatever :P
    return None

entries = []  

with open(r'C:\Users\munas\Documents\data-prep\data_cleaning\alumni_anonymized.csv') as records:
    reader = csv.reader(records)
    next(reader)
    count=0
    for row in reader:
        if row[1]:
            new_row = dict()
            new_row['Exit_Year'] = filter_exit_year(fill_year(row[1]))
            new_row['Last_Name'] = row[0]
            new_row['Id_Number'] = row[3]
            new_row['Birth_Year'] = filter_birth_year(clean_dob(row[4]))
            entries.append(new_row)
            count += 1

entries = [row for row in entries if row['Exit_Year'] is not None and row['Birth_Year'] is not None]


with open(r'C:\Users\munas\Documents\data-prep\data_cleaning\alumni_clean.csv', 'w', newline='') as new_file:
    csv_writer = csv.DictWriter(new_file, fieldnames=['Last_Name', 'Exit_Year', 'Id_Number', 'Birth_Year', 'Age_At_Exit'])
    csv_writer.writeheader()
    csv_writer.writerows(entries)

df = pd.DataFrame(entries, columns=['Last_Name', 'Exit_Year', 'Id_Number', 'Birth_Year', 'Age_At_Exit'])
df = df.set_index('Id_Number')
df = df.dropna(subset=["Exit_Year"])
df = df.dropna(subset=["Birth_Year"])
df["Exit_Year"] = df["Exit_Year"].astype(int)
df["Birth_Year"] = df["Birth_Year"].astype(int)
df["Age_At_Exit"] = (df["Exit_Year"]-df["Birth_Year"]).astype(int)

if __name__ == '__main__':
    #print(df.head(30))
    print(df['Age_At_Exit'].mean())
