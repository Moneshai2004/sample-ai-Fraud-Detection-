# database/db_setup.py
import psycopg2

def create_connection():
    conn = psycopg2.connect(
        database="fraud_detection",
        user="username",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn
