import pandas as pd
from googlesearch import search
# LinkedIn scares me from doing it from bs4 import BeautifulSoup
# Ditto import requests
from openpyxl import Workbook
import csv
import os

# Count files in folder for custom csv numbering (for file generation)

# folder path
dir_path = r'C:/Users/dan.serban/Desktop/Jupyter Data Analysis'
count = 0

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)

# Excel
os.chdir('C:/Users/dan.serban/Desktop/Jupyter Data Analysis')

excel_data = pd.read_excel('data_it_companies_2023.xlsx')
filtered_data = excel_data.iloc[1:, 0].dropna().astype(str).str.strip()
filtered_data = filtered_data[filtered_data.str.len() > 1]

print(filtered_data)

# Perform Google Searches and Extract LinkedIn URLs
linkedin_urls = []
num_results = 1  # Specify the desired number of search results per company

for company_name in filtered_data:
    search_query = company_name + " LinkedIn page"
    results = search(search_query, num=num_results, stop=num_results)
    print(company_name)
    for url in results:
        linkedin_urls.append(url)
        print(url)
        break

workbook = Workbook()
sheet = workbook.active
sheet.title = 'LinkedIn URLs'
for i, url in enumerate(linkedin_urls):
    sheet.cell(row=i + 1, column=1, value=url).hyperlink = url
workbook.save('linkedin_urls.xlsx')

with open('linkedin_urls2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['LinkedIn URLs', 'Company name'])
    for company_name, url in zip(filtered_data, linkedin_urls):
        writer.writerow([url, company_name])


