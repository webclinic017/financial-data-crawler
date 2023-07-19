from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)  # using python codes to manipulate Chrome browser
# driver = webdriver.Chrome(ChromeDriverManager().install())


url = "https://www.naver.com"
driver.get(url)
