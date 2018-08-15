from selenium import webdriver 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
driver_option = webdriver.ChromeOptions()
chromedriver_path =r'C:/Users/pranjal/Desktop/softwares/chromedriver/chromedriver_win32/chromedriver.exe' 
def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path) 

browser = create_webdriver()
browser.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
# Extract rankings of first player
rankings = browser.find_elements_by_xpath("//tr[@class='table-body rankings-table__hero']")
# Extract information for each project
rankings_odi_bat = {}
i=0
for rank in rankings:
    rank_name = rank.text
    rankings_odi_bat[i] = rank_name
    i=i+1
# Extract rankings from 2 to 100
rankings = browser.find_elements_by_xpath("//tr[@class='table-body']")
# Extract information for each project
i=1
for rank in rankings:
    rank_name = rank.text
    rankings_odi_bat[i] = rank_name
    i=i+1

import pandas as pd
# Extracting data
rankings_df = pd.DataFrame.from_dict(rankings_odi_bat, orient = 'index')
# Manipulate the table
rankings_df.columns = [ 'ODI Batting rankings-Men']
rankings_df = rankings_df.reset_index(drop=True)

#------------------------------------------------------------------------------------------------------------------

browser.get("https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/batting")
# Extract rankings of first player
rankings = browser.find_elements_by_xpath("//tr[@class='table-body rankings-table__hero']")
# Extract information for each project
rankings_t20_bat = {}
i=0
for rank in rankings:
    rank_name = rank.text
    rankings_t20_bat[i] = rank_name
    i=i+1
# Extract rankings from 2 to 100
rankings = browser.find_elements_by_xpath("//tr[@class='table-body']")
# Extract information for each project
i=1
for rank in rankings:
    rank_name = rank.text
    rankings_t20_bat[i] = rank_name
    i=i+1

# Extracting data
rankings_df2 = pd.DataFrame.from_dict(rankings_t20_bat, orient = 'index')
# Manipulate the table
rankings_df2.columns = [ 'T20 Batting rankings-Men']
rankings_df2 = rankings_df2.reset_index(drop=True)

#------------------------------------------------------------------------------------------------------------------

browser.get("https://www.icc-cricket.com/rankings/mens/player-rankings/test/batting")
# Extract rankings of first player
rankings = browser.find_elements_by_xpath("//tr[@class='table-body rankings-table__hero']")
# Extract information for each project
rankings_test_bat = {}
i=0
for rank in rankings:
    rank_name = rank.text
    rankings_test_bat[i] = rank_name
    i=i+1
# Extract rankings from 2 to 100
rankings = browser.find_elements_by_xpath("//tr[@class='table-body']")
# Extract information for each project
i=1
for rank in rankings:
    rank_name = rank.text
    rankings_test_bat[i] = rank_name
    i=i+1
browser.quit()

# Extracting data
rankings_df1 = pd.DataFrame.from_dict(rankings_test_bat, orient = 'index')
# Manipulate the table
rankings_df1.columns = [ 'Test Batting rankings-Men']
rankings_df1 = rankings_df1.reset_index(drop=True)

#------------------------------------------------------------------------------------------------------------------

ranking_df_men=pd.DataFrame()
#combine=[rankings_df1 , rankings_df]
ranking_df_men['Test Batting rankings-Men']=rankings_df1['Test Batting rankings-Men']
ranking_df_men['ODI Batting rankings-Men']=rankings_df['ODI Batting rankings-Men']
ranking_df_men['T20i Batting rankings-Men']=rankings_df2['T20 Batting rankings-Men']
print(ranking_df_men)
