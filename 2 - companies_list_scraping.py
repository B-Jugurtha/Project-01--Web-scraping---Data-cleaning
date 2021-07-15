import os
from bs4 import BeautifulSoup as bs
import re
import sys
import glob
from pathlib import Path

pwd = os.getcwd()

# Create raw_data folder
Path(pwd + '/raw_data').mkdir(parents=True, exist_ok=True)

# Create and Initialize csv file:
with open(pwd + '\\raw_data\Data - IT_Companies_Algiers_Raw.csv', 'w', encoding='utf-8') as file:
    file.write('company_id,company_name,city,announce_date')

files = glob.glob(pwd + '\pages\*.html', recursive=False)
# Iterating throw \pages files:
for i, f in enumerate(files):
    with open(f, encoding='utf-8') as file:
        soup = bs(file, 'html.parser')

    announce_div = soup.find_all('div', class_='annonce_store')

    try:
        for elm in announce_div:
            city = elm.find('span', class_='titre_wilaya')
            announce_date = elm.find('p', class_='annonce_date')
            company_name = elm.find(
                'p', class_="annonce_client_name").find('a', class_="name", href=True)
            company_id = company_name.get('href')
            try:
                id = re.search('id=(\w+)', company_id).group(1)
                company_id = id
            except AttributeError:
                company_id = ''

            with open(pwd + '\\raw_data\Data - IT_Companies_Algiers_Raw.csv', 'a', encoding='utf-8') as file:
                file.write('\n')
                file.write(company_id + ',' + company_name.string +
                           ',' + city.string + ',' + announce_date.string)
        print('finished with page: ' + str(i))
    except:
        print("Unexpected error:", sys.exc_info())
