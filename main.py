from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd




option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 2}
)

driver = webdriver.Chrome(
    chrome_options=option, executable_path="C:\\Users\\talha\\chromedriver.exe"
)


# driver = webdriver.Chrome('C:\\Users\\talha\\chromedriver.exe')

driver.get('https://www.facebook.com')
driver.implicitly_wait(10)
email=driver.find_element(By.ID,"email")
email.send_keys("")
password = driver.find_element(By.ID,"pass")
password.send_keys("")
login= driver.find_element(By.NAME,"login")
login.click()
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/label/input").send_keys('tourism')
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div/label/input").send_keys(Keys.ENTER)
print('h')

driver.get('https://www.facebook.com/search/groups?q=tourism&sde=AbotKqEx6VFO7Xg9wiFDgE3hDSnw1teizHLB49vZpXF3bLbxyZ0OOuvrfrGEGCpzofDakrn8opGG9ML5UM4eRoBs')
print('n')
time.sleep(2)
count=len(driver.find_elements(By.XPATH,"//div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld')]"))
print(count)
details=[]
i = 0
try:
    while True:
        time.sleep(0.2)  # depends on internet speed
        groups = driver.find_elements(By.XPATH,"//div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", groups[i])
        print(groups[i].text)
        group_dict = {'group': groups[i].text}
        details.append(group_dict)
        df = pd.DataFrame(details)
        i += 1
except Exception as e:
    print(e)

print(i)  # Gives the count of groups

df.to_csv('output.csv')
driver.close()
