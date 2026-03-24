import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_PASSWORD"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )