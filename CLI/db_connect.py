import sqlite3

def db_connect():
    db_path = '../SERVER/db/tkinter.db'  # Replace with the desired SQLite database file path
    conn = sqlite3.connect(db_path)
    return conn