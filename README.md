# Vulnerable-Web-Application---Course-Project-1-Helsinki-Fi-
This is a deliberately vulnerable web application created for educational purposes. It demonstrates 5 security flaws from the OWASP Top 10 2021 list. WARNING: This application contains intentional security vulnerabilities. DO NOT deploy this to production or any public-facing environment.


OWASP Top 10 2021 Flaws Implemented

A01:2021 - Broken Access Control
A02:2021 - Cryptographic Failures
A03:2021 - Injection (SQL Injection)
A05:2021 - Security Misconfiguration
A07:2021 - Identification and Authentication Failures

Additionally: Cross-Site Request Forgery (CSRF) - included due to its fundamental nature
Prerequisites

Python 3.8 or higher
pip (Python package installer)

Installation Instructions
Windows

Install Python:

Download Python from https://www.python.org/downloads/
During installation, check "Add Python to PATH"


Open Command Prompt and navigate to project directory:

cmd   cd path\to\project

Create virtual environment:

cmd   python -m venv venv
   venv\Scripts\activate

Install dependencies:

cmd   pip install -r requirements.txt
Linux

Install Python (if not already installed):

bash   sudo apt-get update
   sudo apt-get install python3 python3-pip python3-venv

Navigate to project directory:

bash   cd /path/to/project

Create virtual environment:

bash   python3 -m venv venv
   source venv/bin/activate

Install dependencies:

bash   pip install -r requirements.txt
macOS

Install Python (using Homebrew):

bash   brew install python3

Navigate to project directory:

bash   cd /path/to/project

Create virtual environment:

bash   python3 -m venv venv
   source venv/bin/activate

Install dependencies:

bash   pip install -r requirements.txt
Running the Application
Initial Setup (First Time Only)

Apply database migrations:

bash   python manage.py migrate

Create a superuser (admin account):

bash   python manage.py createsuperuser
Follow the prompts to set username, email, and password.

Load sample data (optional):

bash   python manage.py loaddata sample_data.json
Starting the Server
bashpython manage.py runserver
The application will be available at: http://127.0.0.1:8000/
Default Test Accounts
After loading sample data:

User 1: username: alice, password: password123
User 2: username: bob, password: password123
Admin: Use the superuser account you created

Application Features

User registration and login
Personal notes management
User profile viewing
Admin panel (for superusers)
Search functionality

Security Flaws Documentation
Each flaw is documented in the source code with:

Comment explaining the vulnerability
The vulnerable code
The fix (commented out)
References to OWASP documentation

Viewing the Flaws

Broken Access Control - notes/views.py - view_user_notes()
Cryptographic Failures - notes/models.py - Password storage
SQL Injection - notes/views.py - search_notes()
Security Misconfiguration - vulnerable_app/settings.py - DEBUG and SECRET_KEY
Authentication Failures - notes/views.py - login_view()
CSRF - notes/templates/notes/delete_note.html and notes/views.py

Project Structure
vulnerable_app/
├── manage.py
├── requirements.txt
├── README.md
├── sample_data.json
├── vulnerable_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── notes/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    └── templates/
        └── notes/
            ├── base.html
            ├── home.html
            ├── login.html
            ├── register.html
            ├── notes.html
            ├── user_notes.html
            ├── search.html
            └── delete_note.html
            
Stopping the Server
Press Ctrl+C in the terminal where the server is running.

Deactivating Virtual Environment
bashdeactivate

Security Warning
IMPORTANT: This application is intentionally vulnerable and should NEVER be deployed to a production environment or exposed to the internet. It is designed solely for educational purposes to demonstrate common security vulnerabilities.
