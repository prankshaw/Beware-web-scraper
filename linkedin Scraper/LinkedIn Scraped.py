# Just run the following cells to scrape data from your LinkedIn profile (or anyone's, if you know their password :) ). 
# Replace the content of "config.txt" file with the desired username or password to let it automatically fill duing login. 
# Also remember to change the path of driver (mentioned in the cell), to your own location in Line 12. 
# Change to your own LinkedIn username in line 30
# This particular wrapper scrapes the information data like name, connections, profile titile, location from the LikedIn profile and can easily be extended to other sections of profile.  
# Now, you only require to have selenium and chrome driver installed in your machine and start have fun!!


import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('C:/SomeLocation/chromedriver/chromedriver_win32/chromedriver.exe') # Change the location of chromedriver Here
browser.get('https://www.linkedin.com/uas/login')
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]


elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()


link = 'https://www.linkedin.com/in/myusername/'    #Change it to your own username
browser.get(link)

SCROLL_PAUSE_TIME = 5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

for i in range(3):
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

src = browser.page_source
soup = BeautifulSoup(src, 'lxml')
#soup


name_div = soup.find('div', {'class': 'flex-1 mr5'})
#name_div

name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()
#name

loc = name_loc[1].find('li').get_text().strip()
#loc

profile_title = name_div.find('h2').get_text().strip()
#profile_title

connection = name_loc[1].find_all('li')
connection = connection[1].get_text().strip()
#connection

info = []
info.append(link)
info.append(name)
info.append(profile_title)
info.append(loc)
info.append(connection)
print(info)

browser.quit()
