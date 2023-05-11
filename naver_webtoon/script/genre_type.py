from bs4 import BeautifulSoup
import requests
import pandas as pd
#from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def get_URL():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome('/Users/andy/Desktop/github/DE_project/naver_webtoon/chromedriver', options=chrome_options)
    URL = f"https://comic.naver.com/webtoon?tab=genre"  
    driver.get(URL)
    return time.sleep(10)



def get_genre():
    global genres
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    data = soup.find_all('button', attrs={"class" : "TagGroup__tag--xu0OH"})

    genres = []
    for button in data:
        text = button.text.replace("#", "")
        genres.append(text)
    
    driver.quit()

    return genres


def get_genreID():
    global genreID
    genreID = []

    for genre in genres:
        if genre == '로맨스':
            genreID.append('PURE')
        
        elif genre == '판타지':
            genreID.append('FANTASY')
            
        elif genre == '액션':
            genreID.append('ACTION')
            
        elif genre == '일상':
            genreID.append('DAILY')
            
        elif genre == '스릴러':
            genreID.append('THRILL')
            
        elif genre == '개그':
            genreID.append('COMIC')
            
        elif genre == '무협/사극':
            genreID.append('HISTORICAL')
            
        elif genre == '드라마':
            genreID.append('DRAMA')
            
        elif genre == '감성':
            genreID.append('SENSIBILITY')
            
        elif genre == '스포츠':
            genreID.append('SPORTS')
            
        elif genre == '연도별웹툰':
            genreID.append('PERIOD')
            
        elif genre == '브랜드웹툰':
            genreID.append('BRAND')
        
        else:
            new_genre = genre.replace(' ', '+').replace('&', '%26')
            genreID.append(new_genre)

    return genreID

def get_genre_url():
    global genre_url
    genre_url = []
    
    url = f'https://comic.naver.com/webtoon?tab=genre&genre='
    for gen_id in genreID:
        genre_url.append(url + gen_id)
        
    return genre_url


def get_csv():
    df = pd.DataFrame({'genre': genres, 'genreID': genreID, 'genreURL' : genre_url})
    df.index += 1
    df.to_csv(f'../data/webtoon_genre_type.csv', index_label='index')


if __name__ == "__main__":
    get_URL()
    get_genre()
    get_genreID()
    get_genre_url()
    get_csv()

    