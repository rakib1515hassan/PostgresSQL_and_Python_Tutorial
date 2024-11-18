import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from rich.table import Table
from rich.console import Console
import datetime

# Load environment variables
load_dotenv() 

# Set base directory path
BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the connection object from db_connection.py
from db_connection import connection


def get_all_users():
    try:
        cursor = connection.cursor()

        # SQL query to retrieve all users
        select_query = """
        SELECT id, email, first_name, last_name, phone, gender, religion, dob, image, created_at, updated_at
        FROM users;
        """
        
        # Execute the query to retrieve all users
        cursor.execute(select_query)
        
        # Fetch all results
        users = cursor.fetchall()
        
        if users:
            print(f"Found {len(users)} users.")
            return users
        else:
            print("No users found.")
            return []

    except Exception as e:
        print(f"Error retrieving users: {e}")
        return []

    finally:
        cursor.close()


from datetime import datetime

def display_users_in_table(users):
    # Initialize the console for printing
    console = Console()

    # Create the table with a title
    table = Table(title="User Data")

    # Add columns with styles
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Email", style="magenta")
    table.add_column("Name", style="green")
    table.add_column("Phone", style="blue")
    table.add_column("Gender", style="yellow")
    table.add_column("Religion", style="magenta")
    table.add_column("DOB", justify="right", style="green")
    table.add_column("Image", style="blue")
    table.add_column("Created At", style="yellow")
    table.add_column("Updated At", style="yellow")

    # Add rows to the table
    for v in users:
        # Format dates properly
        dob = v[7].strftime('%Y-%m-%d') if isinstance(v[7], datetime.date) else "N/A"
        created_at = v[8] if isinstance(v[8], str) else v[8].strftime('%Y-%m-%d %H:%M:%S')
        updated_at = v[9] if isinstance(v[9], str) else v[9].strftime('%Y-%m-%d %H:%M:%S')
        image = v[8] if v[8] else "N/A"  # If image is None, show N/A
        
        # Add the user row to the table
        table.add_row(str(v[0]), v[1], f"{v[2]} {v[3]}", v[4], v[5], v[6], dob, image, created_at, updated_at)

    # Print the table in the console
    console.print(table)




# Example usage
users = get_all_users()
if users:
    display_users_in_table(users)
