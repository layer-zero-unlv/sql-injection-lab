# SQL Injection Practice Lab

A deliberately vulnerable Flask web application designed for learning and practicing SQL injection techniques. Originally created for a cybersecurity workshop by Layer Zero at UNLV, this project provides a safe environment to understand and exploit SQL injection vulnerabilities.

⚠️ **EDUCATIONAL USE ONLY** - This application contains intentional security vulnerabilities and should never be deployed in a production environment.

## 📑 Table of Contents

- [Learning Objectives](#-learning-objectives)
- [Prerequisites](#️-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Practice Challenges](#-practice-challenges)
- [Hints](#️-hints)
- [Project Structure](#-project-structure)
- [Vulnerable Code Patterns](#-vulnerable-code-patterns)
- [Learning Outcomes](#️-learning-outcomes)
- [Quick Start](#-quick-start)
- [Additional Resources](#-additional-resources)
- [Security Reminders](#-security-reminders)

## 🎯 Learning Objectives

- Understand how SQL injection vulnerabilities occur
- Learn to identify vulnerable code patterns  
- Practice exploiting SQL injection to bypass authentication

## 🛠️ Prerequisites

- Python 3.7 or higher
- Basic understanding of SQL and web applications
- Familiarity with command line/terminal

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/layer-zero-unlv/sql-injection-lab.git
   cd sql-injection-practice
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the database:**
   ```bash
   python create_db.py
   ```
   This creates `users.db` with sample user data from `users.json`.

4. **Start the application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 🎮 Practice Challenges

### Normal Usage
- Visit the homepage and click "Get Started"
- Try logging in with legitimate credentials (check `users.json` for valid usernames)
- Explore the dashboard and user search functionality

### SQL Injection Challenges

**Challenge 1: Authentication Bypass**
- Can you log in without knowing a valid password?
- Examine the login form and consider how SQL queries might be constructed

**Challenge 2: Information Disclosure**
- Use the search functionality to reveal information beyond what's intended
- Try different search patterns and special characters

**Challenge 3: Privilege Escalation**
- Find a way to gain admin privileges
- Look for the admin user and capture the flag!

## 🕵️ Hints

- Pay attention to error messages and SQL query logs in the terminal
- The search feature says "Try SQL injection 😉" when no results are found
- Admin users have access to special flags
- Think about how user input is processed in SQL queries

## 📁 Project Structure

```
├── app.py
├── create_db.py
├── users.json
├── users.db
├── requirements.txt
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    ├── index.html
    ├── login.html
    ├── dashboard.html
    └── 404.html
```

## 🔍 Vulnerable Code Patterns

This application demonstrates several dangerous practices:

- **Unparameterized SQL queries** - Direct string concatenation
- **Insufficient input validation** - User input used directly in queries  
- **Information leakage** - SQL errors exposed to users
- **Weak session management** - Minimal authentication checks

## 🛡️ Learning Outcomes

After practicing with this application, you should understand:

- How SQL injection occurs and why it's dangerous
- The difference between parameterized and vulnerable queries
- Common SQL injection payloads and techniques
- The importance of input validation and prepared statements
- How to identify and test for SQL injection vulnerabilities

## ⚡ Quick Start

```bash
# Clone, setup, and run
git clone https://github.com/layer-zero-unlv/sql-injection-lab.git && cd sql-injection-practice
pip install -r requirements.txt
python create_db.py
python app.py
```

Then visit `http://localhost:5000` to begin practicing!

## 🎓 Additional Resources

- **OWASP SQL Injection Guide:** [https://owasp.org/www-community/attacks/SQL_Injection]
- **SQLite Documentation:** [https://www.sqlite.org/lang.html]
- **Flask Security Best Practices:** [https://flask.palletsprojects.com/en/stable/web-security/]

## 🔒 Security Reminders

- This is a practice environment with intentional vulnerabilities
- Never use these techniques against systems without proper authorization
- Always practice ethical hacking and responsible disclosure
- In real applications, always use parameterized queries and input validation

## 📄 License & Liability

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

**Liability Disclaimer:** Layer Zero UNLV and its members are not liable for any misuse of this educational tool. Users are solely responsible for ensuring their activities comply with applicable laws and regulations. This software is provided "as is" without warranty of any kind.

---

**Created by Layer Zero**
