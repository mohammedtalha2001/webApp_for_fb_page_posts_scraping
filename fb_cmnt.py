from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.chrome.options import Options
import time
import mysql.connector



cnx = mysql.connector.connect(user='root',
                              password='123456',
                              host='localhost',
                              database='new_schema')

# Create a cursor object
cursor = cnx.cursor()


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
email.send_keys("ktalha74@yahoo.com")
password = driver.find_element(By.ID,"pass")
password.send_keys("happybirthday2u")
login= driver.find_element(By.NAME,"login")
login.click()

time.sleep(1)
driver.get("https://www.facebook.com/groups/254658047883386/permalink/5947031248646009")


poster = driver.find_element(By.XPATH,"//h3[contains(@class,'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x1gslohp x1yc453h')]/span/strong[1]").text
print(poster)
desc=""

try:
    desc = driver.find_element(By.XPATH,"//div[contains(@class,'x1iorvi4 x1pi30zi x1l90r2v x1swvt13' )and contains(@id,'jsc_c_a6')]").text

except:
    desc="no description"

print(desc)
arr=[]
i = 0
try:
    while True:

        comments=driver.find_elements(By.XPATH,"//div[contains(@class,'x1tlxs6b x1g8br2z x1gn5b1j x230xth x9f619 xzsf02u x1rg5ohu xdj266r x11i5rnm xat24cr x1mh8g0r x193iq5w x1mzt3pk x1n2onr6 xeaf4i8 x13faqbe xmjcpbm')]")
        arr.append(comments[i].text)
        print(comments[i].text)
        print(arr)
        grpid=123
        query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`)VALUES(%s,%s,%s,%s)'
        data=[grpid,poster,desc,arr[i]]
        cursor.execute(query, data)
        cnx.commit()
        i+=1



except:
    print("done")

query = "SELECT * FROM `new_schema`.`comments`"
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Loop through the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
cnx.close()