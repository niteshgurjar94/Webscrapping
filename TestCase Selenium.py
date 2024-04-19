#Test case:
# 1) Open Web browser (Chrome/Firefox/IE).
# 2) Open URL
# 3) Provide Email
# 3) Provide Password
# 5) click on login.
# 6) Capture title of the dashband page. (Actual title)
# 7) Verify title of the page: "Dashboard/no commerce administartion"
# 8) Close browser
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import pandas as pd
import time

#chrome_binary = "Binaries/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing"
#options = webdriver.ChromeOptions()
#options.binary_location = chrome_binary

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.adamchoi.co.uk/overs/detailed")

all_matches_button = driver.find_element(By.XPATH,"//*[@id='page-wrapper']/div/home-away-selector/div/div/div/div/label[2]")
all_matches_button.click()
dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)




matches = driver.find_elements(By.TAG_NAME,'tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

driver.quit()

df = pd.DataFrame({'date': date,'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv',index=False)
print(df)