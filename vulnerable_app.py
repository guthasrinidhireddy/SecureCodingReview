"""
SecureCodingReview – Task 3
Author: Gutha Srinidhi
Purpose: Demonstrate vulnerability (vulnerable_app.py)
         and secure coding (secure_app.py)
"""


import sqlite3

def login():
    conn = sqlite3.connect('vuln_app.db')
    cursor = conn.cursor()

    username = input("Enter username: ")

    #⚠️ Vulnerable query (no password check)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        print("\n✅ Login successful!")
    else:
        print("\n❌ Login failed!")

    conn.close()

if __name__ == "__main__":
    login()
