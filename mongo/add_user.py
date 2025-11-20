import mysql.connector

def add_user():
    print("\n--- Add New User ---")

    name = input("Enter user name: ").strip()
    email = input("Enter email: ").strip()

    if not name or not email:
        print("Name and email cannot be empty.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sfils_user",
            password="sfils_pass",
            database="sfils_db"
        )

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()

        print(f"User '{name}' added successfully.")

    except mysql.connector.Error as err:
        print("Error adding user:", err)

    finally:
        if conn.is_connected():
            conn.close()
