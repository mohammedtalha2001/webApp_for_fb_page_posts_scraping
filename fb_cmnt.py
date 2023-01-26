from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.chrome.options import Options
from time import sleep
import mysql.connector
from flask import *
import json
from flask_cors import CORS, cross_origin
import requests
import pyautogui
import subprocess

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# @app.route('/run-python-script', methods=['POST'])
# def run_script():
#         subprocess.run(['python', '-c', 'fb_cmnt.py'])
#         # pyautogui.hotkey('shift', 'f10')
#         # print("it is running")
#         response = make_response('Script run!')
#         response.headers['Access-Control-Allow-Origin'] = '*'
#         return 'Script run successfully!'


@app.route('/send-data', methods=['POST'])
@cross_origin()
def send_data():
    # global input_data1,input_data2
    input_data1 = request.json['input1']
    input_data2 = int(request.json['input2'])
    selected_field = request.json['selectedField']
    response = make_response('Success')
    response.headers['Access-Control-Allow-Origin'] = '*'
    print("page name :" + input_data1, "posts :", input_data2, "comments :" + selected_field)
    url = "https://www.facebook.com/{}".format(input_data1)
    # url = "https://www.facebook.com/{}/posts/{}".format(input_data1, input_data2)
    # url = "https://www.facebook.com/groups/{}/permalink/{}".format(input_data1, input_data2)
    test(url=url, input_data1=input_data1,input_data2=input_data2,selected_field=selected_field)
    print(url)
    return "success"




def test(url,input_data1,input_data2,selected_field):
    global slicing
    cnx = mysql.connector.connect(user='root',
                                  password='123456',
                                  host='localhost',
                                  database='new_schema')

    # Create a cursor object
    cursor = cnx.cursor()
    qry = "TRUNCATE TABLE `new_schema`.`comments`;"
    cursor.execute(qry)
    option = Options()

    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    option.headless = True
    driver = webdriver.Chrome(
        chrome_options=option, executable_path="C:\\Users\\talha\\chromedriver.exe"
    )

    # driver = webdriver.Chrome('C:\\Users\\talha\\chromedriver.exe')

    driver.get('https://www.facebook.com')
    driver.implicitly_wait(10)
    email = driver.find_element(By.ID, "email")
    email.send_keys("")
    password = driver.find_element(By.ID, "pass")
    password.send_keys("")
    login = driver.find_element(By.NAME, "login")
    login.click()

    sleep(1)
    # driver.get("https://www.facebook.com/groups/254658047883386/permalink/5947031248646009")
    driver.get(url)

    # poster = driver.find_element(By.XPATH,"//h3[contains(@class,'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x1gslohp x1yc453h')]/span/strong[1]").text

    # if poster if of fb page then this code will run
    poster = driver.find_element(By.XPATH,"//h2[contains(@class,'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz x1gslohp x1yc453h')]").text
    print(poster)

    try:
        sleep(1)
        y = 500
        for timer in range(0, input_data2+1):
            driver.execute_script("window.scrollTo(0," + str(y) + ")")
            y += 500
            sleep(1)

        # Find the elements containing the post data
        posts = driver.find_elements(By.XPATH,"//div[contains(@class,'x9f619 x1n2onr6 x1ja2u2z x2bj2ny x1qpq9i9 xdney7k xu5ydu1 xt3gfkd xh8yej3 x6ikm8r x10wlt62 xquyuld')]/div/div[8]/div/div[count(div)=4]")
        sleep(1)
        driver.execute_script("window.scrollTo(0, 0);")
        print("no of posts loaded: ", len(posts))
        # Iterate over the posts
        print(input_data2)
        for i, post in enumerate(posts[:input_data2]):
            postid = f"You are seeing the content of post {i + 1} "
            print(postid)
            try:
                sleep(1)
                desc = post.find_element(By.XPATH,".//div[contains(@class,'x1iorvi4 x1pi30zi x1swvt13 x1l90r2v') and contains(@id,'jsc_c')]").text
            except:
                desc = "no description"
            print("description: " + desc)
            try:
                while True:
                    # Find the "Show more comments" button
                    show_more_button = post.find_elements(By.XPATH,
                                                          ".//div[contains(@class,'x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv')]//*[contains(text(),'more comments')]")
                    # Check if the button is present
                    if len(show_more_button) > 0:
                        # Click on the button
                        show_more_button[0].click()
                    else:
                        break
            except Exception as e:
                print(e)
            try:
                sleep(1)
                comments = post.find_elements(By.XPATH,
                                              ".//div[contains(@class,'x1tlxs6b x1g8br2z x1gn5b1j x230xth x9f619 xzsf02u x1rg5ohu xdj266r x11i5rnm xat24cr x1mh8g0r x193iq5w x1mzt3pk x1n2onr6 xeaf4i8 x13faqbe xmjcpbm')]")
                # comment_data = [comment.text for comment in comments[:10]]
                # for comment in comments[:10]:
                #     comments_data = [comment.text]
                #     print("Comments:", comments_data)
                #     grpid = "IMnonstopawara"
                #     query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`,`postid`)VALUES(%s,%s,%s,%s,%s)'
                #     data = [grpid, poster, desc, comment.text, postid]
                #     cursor.execute(query, data)
                #     cnx.commit()
                if selected_field == "10":
                    slicing = comments[:10]
                elif selected_field == "All":
                    slicing = comments

                comment_data = [comment.text for comment in slicing]
                comment_data = json.dumps(comment_data)
                print(len(comment_data))
                if len(comment_data) == 2:
                    comment_data = json.dumps(["no comments in this post"])
                else:
                    comment_data = comment_data
            except Exception as e:
                print(e)
                comment_data = json.dumps(["no comments in this post"])

            print("Comments:", comment_data)
            grpid = input_data1
            query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`,`postid`)VALUES(%s,%s,%s,%s,%s)'
            data = [grpid, poster, desc, comment_data, postid]
            cursor.execute(query, data)
            cnx.commit()

            post_height = post.size['height']
            # Scroll to the next post
            driver.execute_script(f"window.scrollBy(0, {post_height});")

            # Wait for the next post to load
            sleep(1)
        # driver.quit()
        # requests.post("http://localhost:3000/api/selenium-done")
    except Exception as e:
        print(e)

    ## these all commented code is for single post data insertion ##
    # try:
    #     # desc = driver.find_element(By.XPATH,"//div[contains(@class,'x1iorvi4 x1pi30zi x1l90r2v x1swvt13' )and contains(@id,'jsc_c_a6')]").text
    #
    #     desc = driver.find_element(By.XPATH,"//div[contains(@class,'x1iorvi4 x1pi30zi x1l90r2v x1swvt13')]").text
    # except:
    #     desc = "no description"
    #
    # print(desc)
    # arr = []
    # i = 0
    # try:
    #     while True:
    #         comments = driver.find_elements(By.XPATH,
    #                                         "//div[contains(@class,'x1tlxs6b x1g8br2z x1gn5b1j x230xth x9f619 xzsf02u x1rg5ohu xdj266r x11i5rnm xat24cr x1mh8g0r x193iq5w x1mzt3pk x1n2onr6 xeaf4i8 x13faqbe xmjcpbm')]")
    #         arr.append(comments[i].text)
    #         print(comments[i].text)
    #         print(arr)
    #
    #         grpid = "IMnonstopawara"
    #         postid= "pfbid02khjWUnFvPZwd6Q"
    #
    #         query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`,`postid`)VALUES(%s,%s,%s,%s,%s)'
    #         data = [grpid, poster, desc, arr[i], postid]
    #         cursor.execute(query, data)
    #         cnx.commit()
    #         driver.execute_script("arguments[0].scrollIntoView(true);", comments[i])
    #         i += 1
    #
    # except Exception as e:
    #     print(e)
    print("record successfully inserted")
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
    driver.quit()

if __name__ == '__main__':
    print("Hello World")
    app.run(port=8000)
