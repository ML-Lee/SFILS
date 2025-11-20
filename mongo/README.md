\# MongoDB Implementation – SFILS Assignment 2



This folder contains the MongoDB-based version of the SFILS library application.  

It is a port of the MySQL-based app to use MongoDB instead, while keeping the same basic operations:

\- Add users

\- Add books

\- Record borrows

\- List books

\- Search for books



The MongoDB database used for this assignment is:



\- Database: `sfils\_db`

\- Collections:

&nbsp; - `books`

&nbsp; - `users`

&nbsp; - `borrow\_records`



---



\## Prerequisites



To run this version of the application, you need:



\- MongoDB Community Server installed and running on the local machine

&nbsp; - The app assumes MongoDB is available at `mongodb://localhost:27017`

\- MongoDB Compass (optional, for inspecting data)

\- Python 3 installed

\- The `pymongo` library installed:



```bash

python -m pip install pymongo



MongoDB Setup



Start the MongoDB server.



On Windows, MongoDB is typically installed as a service and runs automatically.

If needed, it can be started manually with a command like:



mongod --dbpath C:\\data\\db





The application uses the following MongoDB database and collections:



Database: sfils\_db



Collections:



books



users



borrow\_records



These collections are created automatically the first time documents are inserted by the scripts.



You can also view the data using MongoDB Compass by connecting to:



mongodb://localhost:27017





and opening the sfils\_db database.



Database Connection



All scripts in this folder share a common connection module:



mongo\_connection.py



It contains:



from pymongo import MongoClient



client = MongoClient("mongodb://localhost:27017/")

db = client\["sfils\_db"]



books = db\["books"]

users = db\["users"]

borrow\_records = db\["borrow\_records"]





This ensures every script connects to the same MongoDB database and collections.



Files in This Folder



mongo\_connection.py

Shared connection logic for MongoDB. Defines the db, books, users, and borrow\_records handles.



mongo\_main.py

Text-based main menu that lets the user choose between:



Adding users



Adding books



Borrowing books



Listing books



Searching for books



Exiting the program



mongo\_add\_user.py

Prompts for a user name and email, then inserts a document into the users collection.



mongo\_add\_book.py

Prompts for book details (title, author, genre, year), then inserts a document into the books collection.



mongo\_borrow\_book.py

Prompts for a user name and a book title, then records a borrow event in the borrow\_records collection with the current timestamp.



mongo\_list\_books.py

Reads and prints all documents from the books collection. This is useful for verifying that book data is being stored correctly.



mongo\_search\_books.py

Prompts for a search keyword and searches the books collection by title or author using a case-insensitive text match.



README.md

This documentation file, explaining how to configure MongoDB and run the MongoDB version of the SFILS application.



How to Run the MongoDB Application



Open a terminal or command prompt.



Navigate to this folder:



cd path/to/SFILS/mongo





For example on this system:



cd C:\\Users\\smile\\Documents\\SFILS\\mongo





Make sure MongoDB is running (the sfils\_db database will be created automatically as documents are inserted).



Run the main menu script:



python mongo\_main.py





Use the menu to:



Add users



Add books



Borrow books



List books



Search for books



All data is stored in the MongoDB database sfils\_db and can be inspected at any time using MongoDB Compass.



Notes



This MongoDB implementation is designed to mirror the basic behavior of the MySQL version of the SFILS app from Assignment 1, but using a document-oriented model instead of relational tables.



The focus of this assignment is on demonstrating the ability to connect to MongoDB, perform inserts and queries, and document the setup and usage clearly.

