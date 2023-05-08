from bs4 import BeautifulSoup
import requests
import pandas as pd
#from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_URL(day):
    global driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # driver = webdriver.Chrome('/Users/andy/Desktop/github/DE_project/web_scraping/naver_webtoon/chromedriver', options=chrome_options)
    driver = webdriver.Chrome('../chromedriver.exe')
    URL = f"https://comic.naver.com/webtoon?tab={day}"
    driver.get(URL)
    return time.sleep(10)

def scroll_down():
    scroll_pause_time = 2 # 스크롤을 내릴 때마다 대기시간
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_data(day):
    global df
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = soup.find_all('div', attrs={"class" : "ContentList__info_area--bXx7h"})

    for i in range(len(data)):
        titleName = data[i].findAll('a')[0].findAll('span')[-1].text
        titleID = data[i].find('a', href=True)['href'].split('=')[-1]        
        #titleID = data[i].find('a')['href'].split('=')[-1]
        try:
            authorID = data[i].findAll('a')[1]['href'].split('=')[1]
        except (IndexError, KeyError):
            authorID = data[i].findAll('a')[0]['href'].split('=')[1]
                
        try:
            authorName = data[i].findAll('a')[1].text
        except (IndexError, KeyError):
            authorName = data[i].findAll('a')[0].text
                
        if data[i].findAll('span')[0].text == 'UP' or data[i].findAll('span')[0].text == '휴재':
            rating = data[i].findAll('span')[5].text
        else:
            rating = data[i].findAll('span')[4].text
        
        url = f"https://comic.naver.com{data[i].findAll('a')[0]['href']}"
                
        df = pd.concat([df, pd.DataFrame([[day, titleName, titleID, authorName, authorID, rating, url]],
                                    columns = ['day','titleName', 'titleID', 'authorName', 'authorID','rating', 'url'])], ignore_index=True)
        driver.quit()             

    df.index += 1
    df.to_csv(f'../data/webtoon_{day}_data.csv', index_label='index')


if __name__ == "__main__":
    day = 'finish'
    df = pd.DataFrame(columns=['day','titleName', 'titleID', 'authorName', 'authorID','rating', 'url'])
    get_URL(day)
    scroll_down()
    get_data(day)
    