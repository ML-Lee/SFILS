from mongo_connection import borrow_records
from datetime import datetime

user = input("Enter user name: ")
book = input("Enter book title: ")

borrow_records.insert_one({
    "user_name": user,
    "book_title": book,
    "borrow_date": datetime.now()
})

print("Borrow record added to MongoDB!")

