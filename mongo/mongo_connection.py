from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sfils_db"]

books = db["books"]
users = db["users"]
borrow_records = db["borrow_records"]
