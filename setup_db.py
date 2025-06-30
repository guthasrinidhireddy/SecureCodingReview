# --- setup_db.py ---
# This file creates the database and inserts a sample user

import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("vuln_app.db")
cursor = conn.cursor()

# Create a simple 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
''')

# Insert a sample user
cursor.execute("INSERT INTO users VALUES (?, ?)", ("srinidhi", "lucky"))

conn.commit()
conn.close()

print("Database and table created successfully.")
