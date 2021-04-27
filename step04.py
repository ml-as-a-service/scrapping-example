from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://hoopshype.com/salaries/players/')

players = driver.find_elements_by_xpath('//td[@class="name"]')

players_list = []
for p in range(len(players)):
    players_list.append(players[p].text)

print(players_list)
driver.close()