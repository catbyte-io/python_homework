import sqlite3

# Task 1: Create a New SQLite Database
db_conn = sqlite3.connect('../db/magazines.db')

# Close connection
db_conn.close()
