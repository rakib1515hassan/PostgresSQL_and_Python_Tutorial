import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv() 

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection





def get_user_by_email(email):
    try:
        cursor = connection.cursor()

        # SQL query to retrieve a user by email
        select_query = """
            SELECT id, email, first_name, last_name, phone, gender, religion, dob, image, created_at, updated_at
            FROM users
            WHERE email = %s;
        """
        
        # Execute the query with the provided email
        cursor.execute(select_query, (email,))
        
        # Fetch the result
        user = cursor.fetchone()
        
        if user:
            print(f"User found: {user}")
            return user
        else:
            print("User not found!")
            return None
    
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return None
    
    finally:
        cursor.close()

# Example usage
user = get_user_by_email("rakib1515hassan@gmail.com")
if user:
    print(f"User details: {user}")
