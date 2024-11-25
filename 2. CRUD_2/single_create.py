import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv() 

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection



def insert_user(email, first_name, last_name, phone=None, gender=None, religion=None, dob=None, image=None):
    try:
        cursor = connection.cursor()

        # SQL query to insert a new user
        insert_query = """
        INSERT INTO users (email, first_name, last_name, phone, gender, religion, dob, image)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        cursor.execute(insert_query, (email, first_name, last_name, phone, gender, religion, dob, image))

        # Commit the transaction
        connection.commit()

        # Retrieve the generated user ID
        user_id = cursor.fetchone()[0]
        print(f"User created successfully with ID: {user_id}")

    except Exception as e:
        print(f"Error inserting user: {e}")

    finally:
        cursor.close()



##! Example usage
insert_user(
    email      = "rakib1515hassan@gmail.com", 
    first_name = "Md Rakib", 
    last_name  = "Hassan", 
    phone      = "+8801515612682", 
    gender     = "Male", 
    religion   = "Islam", 
    dob        = "1995-10-20", 
    image      = "media/UserImage/rakib.PNG"
)


# insert_user(
#     email      = "mrhassan@gmail.com", 
#     first_name = "Mr", 
#     last_name  = "Hassan", 
#     phone      = "+8801680764592", 
#     gender     = "Male", 
#     religion   = "Islam", 
#     dob        = "1998-10-20", 
#     # image      = "media/UserImage/rakib.PNG"
# )


# insert_user(
#     email      = "tanin@gmail.com", 
#     first_name = "Md", 
#     last_name  = "Tanin", 
#     phone      = "+8801932717449", 
#     gender     = "Male", 
#     religion   = "Islam", 
#     dob        = "2002-5-13", 
#     # image      = "media/UserImage/rakib.PNG"
# )