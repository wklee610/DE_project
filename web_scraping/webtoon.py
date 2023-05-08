from bs4 import BeautifulSoup
import requests
import pandas as pd
#from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver


driver = webdriver.Chrome('chromedriver.exe')


day = 'tue'
URL = f"https://comic.naver.com/webtoon?tab={day}"
df = pd.DataFrame(columns=['day','titleName', 'titleID', 'authorName', 'authorID','rating', 'url'])

driver.get(URL)
URL = "https://comic.naver.com/webtoon?tab="



df = pd.DataFrame(columns=['day','title', 'authorID', 'authorName','rating', 'url'])


    #webtoon_page = requests.get(URL + day)
    
soup = BeautifulSoup(driver.page_source, 'html.parser')
data = soup.find_all('div', attrs={"class" : "ContentList__info_area--bXx7h"})

for i in range(len(data)):
    
    title = data[i].findAll('a')[0].findAll('span')[-1].text
    
    try:
        authorID = data[i].findAll('a')[1]['href'].split('=')[1]
    except IndexError:
        authorID = data[i].findAll('a')[0]['href'].split('=')[1]
    
    try:
        authorName = data[i].findAll('a')[1].text
    except IndexError:
        authorName = data[i].findAll('a')[0].text
    
    rating = data[i].findAll('span')[5].text
    url = f"https://comic.naver.com{data[i].findAll('a')[0]['href']}"
    
    # df = pd.DataFrame(columns=['day','title', 'authorID', 'authorName','rating', 'url'])
    df = pd.concat([df, pd.DataFrame([[day, title, authorID, authorName, rating, url]],
                                    columns = ['day', 'title', 'authorID', 'authorName', 'rating', 'url'])], ignore_index=True)
        
df.index += 1
df.to_csv('../data/webtoon_tue_data.csv', index_label='index')
