import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    conn = pymysql.connect(
        host=os.getenv("MYSQLHOST"),
        user="root",
        password=os.getenv("MYSQLPASSWORD"),
        database=os.getenv("MYSQLDATABASE"),
        port=int(os.getenv("MYSQLPORT")),
        cursorclass=pymysql.cursors.Cursor
    )
    return conn