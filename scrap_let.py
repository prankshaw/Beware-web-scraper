
from selenium import webdriver 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException 
driver_option = webdriver.ChromeOptions()
chromedriver_path =r'C:/Users/pranjal/Desktop/softwares/chromedriver/chromedriver_win32/chromedriver.exe' # change the path here
def create_webdriver():
    return webdriver.Chrome(executable_path=chromedriver_path) 

browser = create_webdriver()
browser.get("https://github.com/topics/c")
# Extract all projects
projects = browser.find_elements_by_xpath("//h3[@class='f3']")
# Extract information for each project
project_list = {}
for proj in projects:
    proj_name = proj.text 
    proj_url = proj.find_elements_by_xpath("a")[0].get_attribute('href') 
    project_list[proj_name] = proj_url
browser.quit()

import pandas as pd
# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')
# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)
print(project_df)
