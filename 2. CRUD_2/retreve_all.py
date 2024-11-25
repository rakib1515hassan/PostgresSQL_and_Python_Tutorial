import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2
from rich.table import Table
from rich.console import Console
from datetime import datetime, date 
import json
from pathlib import Path


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





"""
    ##! Display All Data on Consol Table
"""
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
        dob = v[7].strftime('%Y-%m-%d') if isinstance(v[7], date) else "N/A"
        created_at = v[9] if isinstance(v[9], str) else v[9].strftime('%Y-%m-%d %H:%M:%S')
        updated_at = v[10] if isinstance(v[10], str) else v[10].strftime('%Y-%m-%d %H:%M:%S')
        image = v[8] if v[8] else "N/A"  # If image is None, show N/A
        
        # Add the user row to the table
        table.add_row(str(v[0]), v[1], f"{v[2]} {v[3]}", v[4], v[5], v[6], dob, image, created_at, updated_at)

    # Print the table in the console
    console.print(table)





"""
    ##! Save the data to a JSON file
"""
def save_users_to_json(users, file_path="users.json"):

    def serialize(obj):
        """Helper function to serialize datetime and date objects."""
        if isinstance(obj, (datetime, date)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return obj

    try:
        # Serialize users to JSON format
        users_dict = [
            {
                "id"         : user[0],
                "email"      : user[1],
                "name"       : f"{user[2]} {user[3]}",
                "phone"      : user[4],
                "gender"     : user[5],
                "religion"   : user[6],
                "dob"        : serialize(user[7]),
                "image"      : user[8] if user[8] else "N/A",
                "created_at" : serialize(user[9]),
                "updated_at" : serialize(user[10]),
            }
            for user in users
        ]

        # Write the JSON data to a file
        file_path = Path(file_path)
        with file_path.open("w", encoding="utf-8") as json_file:
            json.dump(users_dict, json_file, indent=4, ensure_ascii=False)

        print(f"User data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving users to JSON: {e}")








##? Ensure the script runs only when executed directly
if __name__ == "__main__":
    users = get_all_users()
    if users:

        ##! IF Show Data on table
        display_users_in_table(users)


        ##! Save the users to a JSON file
        save_users_to_json(users)  
