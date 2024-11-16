# create.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  # Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection



"""
1. Create Operation (Insert Data)
In create.py, you can use the INSERT INTO SQL statement to insert data into your PostgreSQL database.

Example (Insert Data):
"""

def create_user(name, email):
    try:
        cursor = connection.cursor()

        # SQL query to insert a new user
        insert_query = """
        INSERT INTO users (name, email) 
        VALUES (%s, %s) 
        RETURNING id;
        """
        cursor.execute(insert_query, (name, email))

        # Commit the transaction
        connection.commit()

        # Retrieve the generated user ID
        user_id = cursor.fetchone()[0]
        print(f"User created successfully with ID: {user_id}")

    except Exception as e:
        print(f"Error creating user: {e}")
    
    finally:
        cursor.close()

# Example usage
create_user("John Doe", "john.doe@example.com")
