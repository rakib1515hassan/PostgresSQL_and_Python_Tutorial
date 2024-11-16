import os
import sys
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  ##! Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

##! Import the connection object from db_connection.py
from db_connection import connection


def create_user_table():
    try:
        cursor = connection.cursor()

        # SQL query to create the users table
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                slug VARCHAR(255) UNIQUE NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                phone VARCHAR(30) UNIQUE NULL,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                gender VARCHAR(10) NULL,
                religion VARCHAR(20) NULL,
                dob DATE NULL,
                image VARCHAR(255) NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """

        # Execute the query to create the table
        cursor.execute(create_table_query)

        # Create the indexes separately
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_phone ON users(phone);")

        # Commit the changes
        connection.commit()

        print("Users table created successfully!")

    except Exception as e:
        print(f"Error creating table: {e}")
    
    finally:
        cursor.close()
        print("\n\n=================================================")
        print("----------PostgreSQL connection is closed.-----------")



# Run the function to create the table
create_user_table()
