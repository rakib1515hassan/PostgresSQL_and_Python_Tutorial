import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv() 

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection


def insert_multiple_users(users):
    """
    Insert multiple users into the database.

    Args:
        users (list of tuples): Each tuple contains user details:
            (email, first_name, last_name, phone, gender, religion, dob, image)
    """
    try:
        cursor = connection.cursor()

        # SQL query to insert a new user
        insert_query = """
        INSERT INTO users (email, first_name, last_name, phone, gender, religion, dob, image)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        
        # Execute the query for multiple users
        cursor.executemany(insert_query, users)

        # Commit the transaction
        connection.commit()

        print(f"{cursor.rowcount} users inserted successfully.")

    except Exception as e:
        print(f"Error inserting users: {e}")
    
    finally:
        cursor.close()



users = [
    ("ratul@example.com",      "Mr", "Ratul", "+8801515612680", "Male", "Islam", "1994-06-05", "media/UserImage/ratul.PNG"),
    ("john.doe@example.com",   "John", "Doe", "+1234567890", "Male", "Christianity", "1985-05-15", "media/UserImage/john.png"),
    ("jane.smith@example.com", "Jane", "Smith", "+9876543210", "Female", "Hinduism", "1990-08-25", None)
]
if __name__ == "__main__":
    insert_multiple_users(users)

