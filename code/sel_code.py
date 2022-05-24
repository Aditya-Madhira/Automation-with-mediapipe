from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def launchBrowser():

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    opt = webdriver.ChromeOptions()
    opt.add_argument("--incognito")
    driver.get(r'https://fmovies.hn/movie/watch-spider-man-no-way-home-full-71326')
    driver.find_element_by_id(r'watch-7178131').click()



    while(True):
        pass



