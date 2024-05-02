import mysql.connector
print (mysql.connector)

db= mysql.connector.connect(
    host="localhost",
    username = 'root'
)
cursor = db.cursor()
# cursor.execute("Create database TestingNew")
print(db)
cursor.execute("create table student")