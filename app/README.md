\# Application – SFILS Assignment 1



This folder contains a simple command-line application built around the MySQL database used in the SFILS project. The goal of this app is to demonstrate basic operations on the library database, such as adding users and books, recording borrows, listing data, and searching.



The app is intended to be run from the command line and uses Python to connect to the `sfils\_db` MySQL database.



---



\## Prerequisites



Before running the application, make sure you have:



\- Python 3 installed  

\- MySQL server installed and running  

\- The `sfils\_db` database created  

\- The required tables created (for example: `books`, `users`, `borrow\_records`) using the SQL scripts in the `scripts/` folder  

\- The Python MySQL client library installed, such as:



```bash

pip install mysql-connector-python



Database Assumptions



The application assumes:



A MySQL database named sfils\_db



Tables such as:



books – information about books



users – information about library users



borrow\_records – which user borrowed which book and when



These tables should be created using the SQL scripts provided in the scripts/ folder (for example, create\_tables.sql) and populated as needed.

How to Run the Application



Open a terminal or command prompt.



Navigate to the app folder of the project. For example:



cd path/to/SFILS/app





Run the main application:



python main.py





Follow the on-screen menu prompts to:



Add users



Add books



Borrow books



List books



Search for books



Files in This Folder

main.py



Entry point for the application.

Typically presents a text-based menu that lets the user choose actions such as adding users, adding books, borrowing books, listing books, or searching.



add\_user.py



Contains logic to add a new user to the users table in the database.

Prompts for user information and inserts a new record into MySQL.



add\_book.py



Contains logic to add a new book to the books table.

Prompts for book details (such as title, author, etc.) and inserts a new record.



borrow\_book.py



Records when a user borrows a book.

Typically interacts with the borrow\_records table and may check that both the user and the book exist.



list\_books.py



Retrieves and displays books from the books table.

Useful for verifying that book records have been added correctly.



search\_books.py



Provides search functionality over the books table.

For example, it might allow searching by title, author, or other fields.



README.md



This documentation file, explaining how to run and understand the application.



