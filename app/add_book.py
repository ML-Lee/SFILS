import mysql.connector

# Get book details from user
title = input("Enter book title: ")
author = input("Enter author name: ")
genre = input("Enter genre: ")
year = input("Enter publication year: ")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="sfils_user",
    password="sfils_pass",
    database="sfils_db"
)

cursor = conn.cursor()

# Insert book into database
query = "INSERT INTO books (title, author, genre, year) VALUES (%s, %s, %s, %s)"
cursor.execute(query, (title, author, genre, year))
conn.commit()

print("✅ Book added successfully!")

conn.close()
