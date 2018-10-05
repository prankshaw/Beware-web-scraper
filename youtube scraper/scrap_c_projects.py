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
browser.get("https://www.youtube.com/feed/trending")
# Extract all projects
projects = browser.find_elements_by_xpath("//div[@class='style-scope ytd-video-renderer']")
# Extract information for each project
project_list = {}
for proj in projects:
    proj_name = proj.text 
    #proj_url = proj.find_elements_by_xpath("a")[0].get_attribute('href') 
    #project_list[proj_name] = proj_url
    #print(proj_name)
browser.quit()


