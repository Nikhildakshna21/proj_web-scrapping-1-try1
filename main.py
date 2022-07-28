from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from tqdm import tqdm

START_URL ="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome('D:\programing\python\class\web scrapper\chromedriver.exe')
browser.get(START_URL)

for a in tqdm(range(100)):
    time.sleep(0.1)

def scrape():
    headers = ["name","distance","mass","radius"]
    star_data = []
    
    soup=BeautifulSoup(browser.page_source, "html.parser")
    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        temp_list = []
        for a in td:
            print(a.string)    
    

scrape()
