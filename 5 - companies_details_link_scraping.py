from bs4 import BeautifulSoup as bs
import pandas as pd
import os

pwd = os.getcwd()

# Initialize csv file:
with open(pwd + '\\raw_data\\Data - IT_Companies_Algiers_Details_Link_Raw.csv', 'w', encoding='utf-8') as file:
    file.write('company_id'+','+'info_page')

# Opening csv file
df = pd.read_csv(pwd + '\\dataframes\\Data - IT_Companies_Algiers.csv')
page_counter = 1

for i in df.index:
    with open(pwd + '\\details_pages\\'+str(df['company_id'][i])+'.html', encoding='utf-8') as file:
        print('openning the file number: ' + str(page_counter))
        soup = bs(file, 'html.parser')
    info = soup.find(id='menu_informations')

    with open(pwd + '\\raw_data\\Data - IT_Companies_Algiers_Details_Link_Raw.csv', 'a', encoding='utf-8') as file:
        file.write('\n')
        file.write(str(df['company_id'][i]) + ',' + str(info.get('href')))

    page_counter += 1
