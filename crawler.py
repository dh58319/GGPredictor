import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL_skeleton = "https://sports.news.naver.com/kbaseball/news/index?date="


def urls():
    year = 2022
    mon = 10
    date = 6
    while year > 2019:
        if date == 1:
            if mon == 1:
                mon = 12
                year -= 1
            else:
                mon -= 1
                if mon in [1, 3, 5, 7, 8, 10, 12]:
                    date = 31
                elif mon == 2:
                    date = 28
                else:
                    date = 30
        else:
            date -= 1
        url = URL_skeleton + str(year) + str(mon).zfill(2) + str(date).zfill(2)
        pubdate = str(year) + str(mon).zfill(2) + str(date).zfill(2)
        yield url, pubdate


article_list = []
news = pd.DataFrame(columns=['title', 'Date'])


def article_Scraping():
    driver = webdriver.Chrome('./chromedriver')
    for link, date in urls():
        for i in range(1, 10):
            driver.get(link + "&page=" + str(i))
            time.sleep(1)
            articles = driver.find_elements(By.CSS_SELECTOR, '#_newsList > ul > li > div > a')
            for article in articles:
                if len(article.text) != 0:
                    news.loc[len(news)] = [article.text, date]

                    article_list.append(article.text)
        driver.quit()
    news.to_csv('./test.csv', sep=',', na_rep='NaN')


article_Scraping()
