import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    """Create a connection to PostgreSQL."""

    connection = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    return connection


if __name__ == "__main__":

    try:
        connection = get_connection()

        print("PostgreSQL connection successful.")

        connection.close()

    except Exception as error:
        print("Database connection failed.")
        print(error)