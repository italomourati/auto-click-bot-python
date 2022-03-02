from importlib.resources import path
from webbrowser import Chrome
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:/Users/italo/AppData/Local/Google/Chrome/User Data Profile 8')
options.add_argument('--profile-directory=Profile 8')
chrome = webdriver.Chrome('./chromedriver/chromedriver', options=options)
chrome.get('https://www.google.com.br')


