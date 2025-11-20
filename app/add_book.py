import mysql.connector

def add_book():
    print("\n--- Add New Book ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    year = input("Enter publication year: ").strip()

    # Basic validation
    if not title or not author:
        print("Title and author cannot be empty.")
        return

    if not year.isdigit():
        print("Publication year must be a number.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sfils_user",
            password="sfils_pass",
            database="sfils_db"
        )

        cursor = conn.cursor()
        query = """
            INSERT INTO books (title, author, genre, year)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, author, genre, year))
        conn.commit()

        print(f"Book '{title}' by {author} added successfully!")

    except mysql.connector.Error as err:
        print("Error adding book:", err)

    finally:
        if conn.is_connected():
            conn.close()
