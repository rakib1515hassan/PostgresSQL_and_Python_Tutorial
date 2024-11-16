"""
    2. Read Operation (Retrieve Data)
    You can retrieve records using the SELECT statement in SQL. You might want to fetch all users or a specific user based on certain criteria.
"""

# retrieve.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection





def get_user_by_id(user_id):
    try:
        cursor = connection.cursor()

        # SQL query to fetch user by ID
        select_query = "SELECT id, name, email, created_at FROM users WHERE id = %s;"
        cursor.execute(select_query, (user_id,))

        # Fetch one result
        user = cursor.fetchone()

        if user:
            print(f"User Found: ID={user[0]}, Name={user[1]}, Email={user[2]}, Created At={user[3]}")
        else:
            print("User not found!")

    except Exception as e:
        print(f"Error retrieving user: {e}")
    
    finally:
        cursor.close()

# Example usage
get_user_by_id(1)  # Replace with an actual user ID



##! You can also use cursor.fetchall() if you want to retrieve all users.

def get_all_users():
    try:
        cursor = connection.cursor()

        # SQL query to fetch all users
        select_query = "SELECT id, name, email, created_at FROM users;"
        cursor.execute(select_query)

        # Fetch all results
        users = cursor.fetchall()

        for user in users:
            print(f"ID={user[0]}, Name={user[1]}, Email={user[2]}, Created At={user[3]}")

    except Exception as e:
        print(f"Error retrieving users: {e}")
    
    finally:
        cursor.close()

# Example usage
get_all_users()
