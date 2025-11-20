from mongo_connection import books

title = input("Enter book title: ")
author = input("Enter author name: ")
genre = input("Enter genre: ")
year = input("Enter publication year: ")

books.insert_one({
    "title": title,
    "author": author,
    "genre": genre,
    "year": year
})

print("Book added to MongoDB!")
