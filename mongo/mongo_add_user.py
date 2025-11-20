from mongo_connection import users

name = input("Enter user name: ")
email = input("Enter email: ")

users.insert_one({
    "name": name,
    "email": email
})

print("User added to MongoDB!")
