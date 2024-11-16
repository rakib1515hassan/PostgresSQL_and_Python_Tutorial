import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  ##! Load environment variables from .env file

BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

##! Import the connection object from db_connection.py
from db_connection import connection






try:
    cursor = connection.cursor()

    # Create a table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    connection.commit()
    print("Table created successfully!")
    
except Exception as e:
    print(f"Error creating table: {e}")
    





finally:
    cursor.close()
    print("\n\n=================================================")
    print("----------PostgreSQL connection is closed.-----------")
