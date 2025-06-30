# SecureCodingReview
Task 3 - Secure Coding Review | CodeAlpha Cybersecurity Internship

SecureCodingReview/
├── vulnerable_app.py     ← Insecure code
├── secure_app.py         ← Fixed version
├── setup_db.py           ← DB setup script
└── README.md             ← Documentation (I'll give you below)



# 🔐 Secure Coding Review – CodeAlpha Cybersecurity Internship

## 📁 Task 3: Secure Coding Review
By **Gutha Srinidhi**  
Internship: CodeAlpha – Cybersecurity Track

---

## ✅ Objective:
Identify and fix vulnerabilities in a sample Python application.

---

## 🔍 Part 1: Vulnerable Application (`vulnerable_app.py`)

### 🔥 Issues Identified:
1. **SQL Injection**  
   - User input is directly injected into the SQL query.
   - Example: `' OR '1'='1` bypasses login.
   
2. **No Password Hashing**  
   - Passwords are stored and compared in plaintext.

3. **No Input Validation**  
   - No checks for username format or malicious strings.

---

## 🛠️ Part 2: Secure Version (`secure_app.py`)

### ✅ Fixes Implemented:
- Used **parameterized queries** (`cursor.execute(...)`) to prevent SQL injection.
- Restored password check for proper authentication.

---

## 🧪 Setup Instructions:
1. Run `setup_db.py` to create `vuln_app.db` with a sample user:
   - **Username**: `srinidhi`
   - **Password**: `lucky`

2. Run `vulnerable_app.py` to test insecure login bypass.

3. Run `secure_app.py` to test the secure version.

---

## 🧠 Tools Used:
- Language: Python
- Database: SQLite
- IDE: Thonny / Terminal
- Static Review (optional): Bandit

---

## ✅ Conclusion:
This task highlights the importance of secure coding practices like:
- Input validation
- Avoiding string interpolation in SQL
- Using parameterized queries

---

🔐 Stay Secure!  
🧑‍💻 Gutha Srinidhi  
CodeAlpha – Cybersecurity Internship
