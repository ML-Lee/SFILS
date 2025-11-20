from mongo_connection import books

for book in books.find():
    print(book)

