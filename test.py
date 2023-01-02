# import mysql.connector
#
# cnx = mysql.connector.connect(user='root',
#                               password='123456',
#                               host='localhost',
#                               database='new_schema')
#
# # Create a cursor object
# cursor = cnx.cursor()
# grpid = 12344
# poster = "ahmed ali rajput"
# desc = "no description"
# comments = ['ggg', 'hhhh', 'jjjj']
# i = 0
# try:
#
#     while True:
#         query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`)VALUES(%s,%s,%s,%s)'
#         data = [grpid, poster, desc, comments[i]]
#         cursor.execute(query, data)
#         cnx.commit()
#         i += 1
#
# except:
#     print("none")
#
# query = "SELECT * FROM `new_schema`.`comments`"
# cursor.execute(query)
#
# # Fetch the results
# results = cursor.fetchall()
#
# # Loop through the results
# for result in results:
#     print(result)
#
# # Close the cursor and connection
# cursor.close()
# cnx.close()



from flask import *
from flask_cors import CORS, cross_origin
import subprocess



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
url=""

@app.route('/run-python-script', methods=['POST'])
def run_script():
  subprocess.run(['python', 'fb_cmnt.py'])
  return 'Script run successfully!'