import mysql.connector
mydb=mysql.connector.connect(
        host="localhost",
        user="pma",
        passwd="localhostpma@123",
        database="criminaldb"
        )

print(mydb)        
        