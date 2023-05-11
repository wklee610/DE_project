from bs4 import BeautifulSoup
import requests
import pandas as pd
#from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def get_URL(URL):
    global driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--window-size=720,1080')
    # driver = webdriver.Chrome('../chromedriver.exe', options=chrome_options)
    driver = webdriver.Chrome('../chromedriver.exe')
    driver.get(URL)
    return time.sleep(6)

def scroll_down():
    scroll_pause_time = 3 # 스크롤을 내릴 때마다 대기시간
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_data(genre, genreID):
    global df
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = soup.find_all('div', attrs={"class" : "ContentList__info_area--bXx7h"})

    for i in range(len(data)):
        titleName = data[i].findAll('a')[0].findAll('span')[-1].text
        titleID = data[i].find('a', href=True)['href'].split('=')[-1]        
        try:
            authorID = data[i].findAll('a')[1]['href'].split('=')[1]
        except (IndexError, KeyError):
            authorID = data[i].findAll('a')[0]['href'].split('=')[1]
                
        try:
            authorName = data[i].findAll('a')[1].text
        except (IndexError, KeyError):
            authorName = data[i].findAll('a')[0].text
                
        df = pd.concat([df, pd.DataFrame([[genre, titleName, titleID, authorName, authorID]],
                                    columns = ['genre','titleName', 'titleID', 'authorName', 'authorID'])], ignore_index=True)
        driver.quit()             

    df.index += 1
    df.to_csv(f'../data/webtoon_{genreID}_data.csv', index_label='index')
    
if __name__ == "__main__":
    df = pd.read_csv('../data/webtoon_genre_type.csv')
    genres = df['genre'].tolist()
    genre_url = df['genreURL'].tolist()
    genreID = df['genreID'].tolist()
    
    for i in range(len(genres)):
        df = pd.DataFrame(columns=['genre','titleName', 'titleID', 'authorName', 'authorID'])
        get_URL(genre_url[i])
        scroll_down()
        get_data(genres[i], genreID[i])
        