from bs4 import BeautifulSoup as bs
from pathlib import Path
import os
import glob
import time
import random
import requests

pwd = os.getcwd()


page_counter = 1
URL = "https://www.example.com/companies/?page="

# Creating 'pages' folder if this one exists deletes it's content
try:
    Path(pwd + '/pages').mkdir(parents=True, exist_ok=False)
except FileExistsError:
    print("File Already exists, Deleting it's content...")
    files = glob.glob(pwd + '/pages/*')
    for f in files:
        os.remove(f)
    time.sleep(5)

while page_counter <= 400:
    page = requests.get(URL+str(page_counter))
    soup = bs(page.content, "html.parser")

    if(page_counter % 10 == 0):
        time.sleep(random.randrange(8, 13))
        print(page_counter)

    with open('pages/'+str(page_counter)+".html", "w", encoding='utf-8') as file:
        file.write(str(soup))

    page_counter += 1
