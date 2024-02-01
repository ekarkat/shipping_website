
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read environment variables
mysql_user = os.getenv("MYSQL_USER")
mysql_pwd = os.getenv("MYSQL_PWD")
mysql_host = os.getenv("MYSQL_HOST")
mysql_db = os.getenv("MYSQL_DB")

# Construct the connection string
connection_string = f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}?charset=utf8"

# Create engine
engine = create_engine(connection_string, pool_pre_ping=True)

# Test the connection
try:
    conn = engine.connect()
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")