import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

load_dotenv()  ##? Load environment variables from .env file


# Add the parent directory to the Python path
BASE_DIR = sys.path.append(str(Path(__file__).resolve().parent.parent))



##! Database Setup
from .db_connection import *


