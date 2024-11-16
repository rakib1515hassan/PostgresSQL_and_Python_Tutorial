import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()  ##? Load environment variables from .env file




##! Database connection parameters
db_config = {
    "host"     : os.getenv("DB_HOST"),      ##? Replace with your PostgreSQL server host
    "database" : os.getenv("DB_NAME"),      ##? Replace with your database name
    "user"     : os.getenv("DB_USER"),      ##? Replace with your username
    "password" : os.getenv("DB_PASSWORD"),  ##? Replace with your password
    "port"     : os.getenv("DB_PORT", 5432) ##? Default PostgreSQL port is 5432
}


try:

    ##! Connect to PostgreSQL database
    connection = psycopg2.connect(**db_config)
    print("----------Database connection successful!------------")




    ##! Create a cursor object
    cursor = connection.cursor()



    ##! Test the connection by executing a query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to: {db_version}")
    print("=================================================\n\n")



    # ##! Close the cursor and connection
    # cursor.close()
    # connection.close()
    # print("\n\n----------PostgreSQL connection is closed.-----------")
    



except Exception as error:
    print("Error connecting to PostgreSQL database:", error)






# finally:
#     # Clean up and close the connection
#     if 'connection' in locals() and connection:
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed.")
