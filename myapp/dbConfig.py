import sqlite3
import os

def create_connection():
    db_path = r"D:\Python\django\explorer_django\Markdown_File_Processor\Project0\db.sqlite3"
    try:
        conn = sqlite3.connect(db_path)
        print("DB connected successfully")
        return conn
    except sqlite3.Error as e:
        print(e) 
