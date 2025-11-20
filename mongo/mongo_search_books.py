from mongo_connection import books

keyword = input("Search keyword: ")

results = books.find({
    "$or": [
        {"title": {"$regex": keyword, "$options": "i"}},
        {"author": {"$regex": keyword, "$options": "i"}}
    ]
})

for book in results:
    print(book)

