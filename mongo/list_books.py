import mysql.connector

def list_books():
    print("\n--- List of Books ---")

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sfils_user",
            password="sfils_pass",
            database="sfils_db"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, genre, year FROM books")
        results = cursor.fetchall()

        if not results:
            print("No books found in the database.")
            return

        print("\nID | Title | Author | Genre | Year")
        print("-----------------------------------------")

        for row in results:
            book_id, title, author, genre, year = row
            print(f"{book_id} | {title} | {author} | {genre} | {year}")

    except mysql.connector.Error as err:
        print("Error retrieving book list:", err)

    finally:
        if conn.is_connected():
            conn.close()
