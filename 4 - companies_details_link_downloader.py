import requests
from bs4 import BeautifulSoup as bs
import time
import random
import os
import pandas as pd
from pathlib import Path

pwd = os.getcwd()
# Creating /details_page folder
Path(pwd + '/details_pages').mkdir(parents=True, exist_ok=True)

df = pd.read_csv(pwd + '\\dataframes\\Data - IT_Companies_Algiers.csv')
URL = "https://www.example.com/profil/?id="
page_counter = 0

for i in df.index:
    page = requests.get(URL + str(df['company_id'][i]))
    soup = bs(page.content, "html.parser")

    # setting a timeout each 10 pages of 8 to 13 seconds
    if(page_counter % 10 == 0 and page_counter != 0):
        time.sleep(random.randrange(8, 13))
        print(page_counter)

    with open('details_pages/'+str(df['company_id'][i])+".html", "w", encoding='utf-8') as file:
        file.write(str(soup))

    print('Finished with page :' + str(page_counter))
    page_counter += 1
