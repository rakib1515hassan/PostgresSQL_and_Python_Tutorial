"""
4. Delete Operation (Delete Data)
The DELETE statement allows you to remove a record from the database.

Example (Delete Data):
"""



# delete.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection

def delete_user(user_id):
    try:
        cursor = connection.cursor()

        # SQL query to delete user by ID
        delete_query = "DELETE FROM users WHERE id = %s;"
        cursor.execute(delete_query, (user_id,))

        # Commit the transaction
        connection.commit()

        # Check if any row was deleted
        if cursor.rowcount > 0:
            print(f"User ID {user_id} deleted successfully!")
        else:
            print(f"No user found with ID {user_id}")

    except Exception as e:
        print(f"Error deleting user: {e}")
    
    finally:
        cursor.close()

# Example usage
delete_user(1)  # Replace with an actual user ID
