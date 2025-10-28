import mysql.connector
from datetime import datetime

# Get borrow details from user
user_id = input("Enter user ID: ")
book_id = input("Enter book ID: ")
borrow_date = datetime.now().strftime('%Y-%m-%d')

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",
    password="sfils_pass",
    database="sfils_db"
)

cursor = conn.cursor()

# Insert borrow record
query = "INSERT INTO borrow_records (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
cursor.execute(query, (user_id, book_id, borrow_date))
conn.commit()

print("✅ Borrow record added successfully!")

conn.close()
