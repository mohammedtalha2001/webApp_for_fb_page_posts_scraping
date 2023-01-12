import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='123456',
                              host='localhost',
                              database='new_schema')

# Create a cursor object
cursor = cnx.cursor()
qry = "TRUNCATE TABLE `new_schema`.`comments`;"
cursor.execute(qry)
# grpid = 12344
poster = "ahmed ali rajput"
desc = "no description"
comments = ['ggg', 'hhhh']
grpid = "IMnonstopawara"
postid = "I love 🍕❤️!"
arr = []


i = 0
try:

    while True:
        # query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`)VALUES(%s,%s,%s,%s)'
        query = 'INSERT INTO `new_schema`.`comments`(`grpid`,`poster`,`description`,`comments`,`postid`)VALUES(%s,%s,%s,%s,%s)'
        data = [grpid, poster, desc, comments[i], postid]
        cursor.execute(query, data)
        cnx.commit()
        i += 1

except:
    print("none")

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


