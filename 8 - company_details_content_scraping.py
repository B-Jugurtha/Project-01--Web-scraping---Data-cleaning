from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import os

pwd = os.getcwd()

# Initialize csv file:
with open(pwd + '\\raw_data\\Data - IT_Companies_Algiers_Details_Raw.csv', 'w', encoding='utf-8') as file:
    file.write('company_id'+','+'address'+','+'phone'+','+'fax'+',' +
               'mail'+','+'website'+','+'facebook_page'+','+'working_hours')
# Opening the dataframe:
df = pd.read_csv(pwd + '\\dataframes\\Data - IT_Companies_Algiers.csv')

for i in df.index:
    # Ignore Unfound Files
    try:
        with open(pwd + '\\details_content_pages\\'+str(df['company_id'][i])+'.html', encoding='utf-8') as file:
            soup = bs(file, 'html.parser')
    except:
        continue

    company_id = address = phone = fax = mail = website = facebook_page = working_hours = ''
    # Catch Errors from incomplete pages
    try:
        info = soup.find(id='informations').find_all('p')

        for elm in info:
            label = elm.find('label')
            if(re.search(r"Adresse", label.string)):
                address = elm.find('span').string
                address = re.sub(r"^\s+|\s+$", "", address)
                address = address.replace(',', ' ')
            elif(re.search(r"Téléphone", label.string)):
                phone = elm.find('span').string
                phone = re.sub(r"^\s+|\s+$", "", phone)
                phone = phone.replace(',', ' ')
            elif(re.search(r"Fax", label.string)):
                fax = elm.find('span').string
                fax = re.sub(r"^\s+|\s+$", "", fax)
                fax = fax.replace(',', ' ')
            elif(re.search(r"Email", label.string)):
                mail = elm.find('span').string
                mail = re.sub(r"^\s+|\s+$", "", mail)
                mail = mail.replace(',', ' ')
            elif(re.search(r"Site Web", label.string)):
                website = elm.find('span').string
                website = re.sub(r"^\s+|\s+$", "", website)
                website = website.replace(',', ' ')
            elif(re.search(r"Page Facebook", label.string)):
                facebook_page = elm.find('span').string
                facebook_page = re.sub(r"^\s+|\s+$", "", facebook_page)
                facebook_page = facebook_page.replace(',', ' ')
            elif(re.search(r"Horaires de travail", label.string)):
                working_hours = elm.find('span').string
                working_hours = re.sub(r"^\s+|\s+$", "", working_hours)
                working_hours = working_hours.replace(',', ' ')

        with open(pwd + '\\raw_data\\Data - IT_Companies_Algiers_Details_Raw.csv', 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(str(df['company_id'][i]) + ',' + str(address) + ',' + str(phone) + ',' +
                       str(fax) + ',' + str(mail) + ',' + str(website) + ',' + str(facebook_page) + ',' + str(working_hours))
        print('Finished with page : ' + str(df['company_id'][i])+'.html')
    except:
        print('Error On page: ' + str(df['company_id'][i])+'.html')
        # Some pages are incomplete and have errors
        with open(pwd + '\\raw_data\\Data - Unavailable_Links.csv', 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(str(df['company_id'][i]) + ',True')
        pass
