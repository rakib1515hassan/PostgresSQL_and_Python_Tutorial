"""
3. Update Operation (Update Data)
The UPDATE statement allows you to modify existing data in the database.

Example (Update Data):
"""

# update.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection

def update_user(user_id, name, email):
    try:
        cursor = connection.cursor()

        # SQL query to update user details
        update_query = """
        UPDATE users 
        SET name = %s, email = %s 
        WHERE id = %s;
        """
        cursor.execute(update_query, (name, email, user_id))

        # Commit the transaction
        connection.commit()

        # Check if any row was updated
        if cursor.rowcount > 0:
            print(f"User ID {user_id} updated successfully!")
        else:
            print(f"No user found with ID {user_id}")

    except Exception as e:
        print(f"Error updating user: {e}")
    
    finally:
        cursor.close()

# Example usage
update_user(1, "Jane Doe", "jane.doe@example.com")  # Replace with actual user data
