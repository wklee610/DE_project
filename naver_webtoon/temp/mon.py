from bs4 import BeautifulSoup
import requests
import pandas as pd
#from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver

#days = ['mon', 'tue', 'wed', 'thu','fri','sat','sun','dailyPlus', 'new', 'finish']
#days = ['mon', 'tue', 'wed', 'thu','fri','sat','sun','dailyPlus', 'new']

day = 'tue'
    
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
# driver = webdriver.Chrome('../chromedriver.exe', options=chrome_options)
driver = webdriver.Chrome('../chromedriver.exe')

URL = f"https://comic.naver.com/webtoon?tab={day}"
df = pd.DataFrame(columns=['day','titleName', 'titleID', 'authorName', 'authorID','rating', 'url'])
driver.get(URL)
requests.get(URL)


soup = BeautifulSoup(driver.page_source, 'html.parser')
data = soup.find_all('div', attrs={"class" : "ContentList__info_area--bXx7h"})


for i in range(len(data)):
    titleName = data[i].findAll('a')[0].findAll('span')[-1].text
            
    titleID = data[i].find('a')['href'].split('=')[-1]
    try:
        authorID = data[i].findAll('a')[1]['href'].split('=')[1]
    except IndexError:
        authorID = data[i].findAll('a')[0]['href'].split('=')[1]
            
    try:
        authorName = data[i].findAll('a')[1].text
    except IndexError:
        authorName = data[i].findAll('a')[0].text
            
    if data[i].findAll('span')[0].text == 'UP' or data[i].findAll('span')[0].text == '휴재':
        rating = data[i].findAll('span')[5].text
    else:
        rating = data[i].findAll('span')[4].text
    
    url = f"https://comic.naver.com{data[i].findAll('a')[0]['href']}"
            
            # df = pd.DataFrame(columns=['day','title', 'authorID', 'authorName','rating', 'url'])
    df = pd.concat([df, pd.DataFrame([[day, titleName, titleID, authorName, authorID, rating, url]],
                                    columns = ['day','titleName', 'titleID', 'authorName', 'authorID','rating', 'url'])], ignore_index=True)

df.index += 1
df.to_csv(f'../data/webtoon_{day}_data.csv', index_label='index')

driver.close()