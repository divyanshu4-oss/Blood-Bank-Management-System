# Creating table into database!!!
import sqlite3

# Connect to sqlite database
def getsqliteconnection():
    conn = sqlite3.connect('bms.sqlite')
    # conn = sqlite3.connect('proj.db')
    print("Connected to SQLite")
    return conn
