import sqlite3

def login():
    conn = sqlite3.connect('vuln_app.db')
    cursor = conn.cursor()

    username = input("Enter username: ")
    # Optional: use password check again if needed
    password = input("Enter password: ")

    # ✅ Safe parameterized query
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

    result = cursor.fetchone()
    if result:
        print("\n✅ Login successful!")
    else:
        print("\n❌ Login failed!")

    conn.close()

if __name__ == "__main__":
    login()
