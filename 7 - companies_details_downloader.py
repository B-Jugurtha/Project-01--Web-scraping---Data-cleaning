import requests
from bs4 import BeautifulSoup as bs
import re
import time
import random
import os
from pathlib import Path
import pandas as pd
from os import path

pwd = os.getcwd()

# Creating /details_content_pages folder
Path(pwd + '\\details_content_pages').mkdir(parents=True, exist_ok=True)

# Opening the dataframe
df = pd.read_csv(
    pwd + '\\dataframes\\Data - IT_Companies_Algiers_With_Details_Links.csv')

# Initializing csv File
with open(pwd + '\\raw_data\\Data - Unavailable_Links.csv', 'w', encoding='utf-8') as file:
    file.write('company_id'+','+'Unavailble_Links')

URL = "https://www.example.com/"
page_counter = 0

for i in df.index:
    regex = '^profil\contact\?id='
    # looking for external links
    if(not path.exists(pwd + '\\details_content_pages\\'+str(df['company_id'][i])+".html")):
        if(re.search(regex, str(df['info_page'][i]))):
            print('downloading : ' + str(df['company_id'][i])+".html")
            page = requests.get(str(URL + df['info_page'][i]))
            soup = bs(page.content, "html.parser")
            with open(pwd + '\\details_content_pages\\'+str(df['company_id'][i])+".html", "w", encoding='utf-8') as file:
                file.write(str(soup))

            # Setting a timeout
            if(page_counter % 10 == 0 and page_counter != 0):
                time.sleep(random.randrange(8, 10))
                print(page_counter)
        else:
            try:
                print('downloading : ' + str(df['company_id'][i])+".html")
                page = requests.get(str(df['info_page'][i]))
                soup = bs(page.content, "html.parser")

                with open(pwd + '\\details_content_pages\\'+str(df['company_id'][i])+".html", "w", encoding='utf-8') as file:
                    file.write(str(soup))

                # Setting a timeout
                if(page_counter % 10 == 0 and page_counter != 0):
                    time.sleep(random.randrange(8, 10))
                    print(page_counter)
            except:
                print('error with ' + str(df['company_id'][i]))
                with open(pwd + '\\raw_data\\Data - Unavailable_Links.csv', 'a', encoding='utf-8') as file:
                    file.write('\n')
                    file.write(str(df['company_id'][i])+','+'True')

    print('Finished with page :' + str(page_counter))
    page_counter += 1
