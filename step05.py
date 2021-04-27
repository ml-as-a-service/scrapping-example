from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://hoopshype.com/salaries/players/')

df = pd.DataFrame(columns=['Player','Salary','Year'])  

for yr in range(1990,2019):
    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements_by_xpath('//td[@class="name"]')
    salaries = driver.find_elements_by_xpath('//td[@class="hh-salaries-sorted"]') 
    
    players_list = []
    for p in range(len(players)):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(len(salaries)):
        salaries_list.append(salaries[s].text)
    
    data_tuples = list(zip(players_list[1:],salaries_list[1:])) 
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary'])
    temp_df['Year'] = yr 
    df = df.append(temp_df) 
    
driver.close()

df.to_csv('player.csv')