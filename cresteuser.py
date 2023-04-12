import sqlite3
import os

# Function to create a connection to the database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('student_data.db')
        print(f"Connected to SQLite database: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a table in the database
def create_table(conn):
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     email TEXT NOT NULL);''')
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

# Function to insert data into the table
def create_user(conn, name, email):
    try:
        conn.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        conn.commit()
        print(f"{name} added to the database")
    except sqlite3.Error as e:
        print(e)

# Function to read data from the table
def read_users(conn):
    try:
        cursor = conn.execute("SELECT * FROM users")
        for row in cursor:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
    except sqlite3.Error as e:
        print(e)

# Function to update data in the table
def update_user(conn, id, name, email):
    try:
        conn.execute(f"UPDATE users SET name='{name}', email='{email}' WHERE id={id}")
        conn.commit()
        print(f"User with ID {id} updated")
    except sqlite3.Error as e:
        print(e)

# Function to delete data from the table
def delete_user(conn, id):
    try:
        conn.execute(f"DELETE FROM users WHERE id={id}")
        conn.commit()
        print(f"User with ID {id} deleted")
    except sqlite3.Error as e:
        print(e)

# Main function to run the project
def main():
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        create_user(conn, "sujal", "sujal879@gmail.com")
        create_user(conn, "saurav", "sauravsuman.kkit@nitk.edu.in")
        read_users(conn)
        update_user(conn, 1, "saurav suman", "suman66@gmail.com")
        read_users(conn)
        delete_user(conn, 2)
        read_users(conn)
    else:
        print("Error: Could not create database connection")

if __name__ == '__main__':
    main()
