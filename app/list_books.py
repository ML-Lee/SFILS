import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",
    password="sfils_pass",
    database="sfils_db"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
