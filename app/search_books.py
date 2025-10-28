import mysql.connector

keyword = input("Enter a keyword to search: ")

conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",
    password="sfils_pass",
    database="sfils_db"
)

cursor = conn.cursor()
query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
for row in cursor.fetchall():
    print(row)

conn.close()
