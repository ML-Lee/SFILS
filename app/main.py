import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",          # ← use the new user you created
    password="sfils_pass",      # ← use the password you set
    database="sfils_db"
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES")
for table in cursor.fetchall():
    print(table)

conn.close()
