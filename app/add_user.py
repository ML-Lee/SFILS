import mysql.connector

name = input("Enter user name: ")
email = input("Enter email: ")

conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",
    password="sfils_pass",
    database="sfils_db"
)

cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
conn.commit()
print("User added.")

conn.close()
