"""
Dynamic Form Application with Database Storage
------------------------------------------------
A Flask web app that captures user input through an HTML form,
validates it, and stores it persistently in a MySQL database.
Implements core CRUD concepts: Create (submit form) and Read (view records).
"""

import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

# ---------------------------------------------------------------------------
# Database configuration
# Set these as environment variables before running, e.g.:
#   export DB_HOST=localhost
#   export DB_USER=root
#   export DB_PASSWORD=yourpassword
#   export DB_NAME=dynamic_form_db
# ---------------------------------------------------------------------------
DB_CONFIG = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "dynamic_form_db"),
}


def get_db_connection():
    """Create and return a new MySQL database connection."""
    return mysql.connector.connect(**DB_CONFIG)


def init_db():
    """Create the submissions table if it doesn't already exist."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS submissions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Error as e:
        print(f"Database initialization error: {e}")


def is_valid_email(email):
    pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return re.match(pattern, email) is not None


@app.route("/")
def index():
    """Render the form page."""
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    """Handle form submission: validate input, then insert into MySQL (Create)."""
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    # Server-side validation (backs up the front-end JS validation)
    errors = []
    if not name:
        errors.append("Name is required.")
    if not email or not is_valid_email(email):
        errors.append("A valid email address is required.")
    if not message:
        errors.append("Message is required.")

    if errors:
        for error in errors:
            flash(error, "error")
        return redirect(url_for("index"))

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO submissions (name, email, message) VALUES (%s, %s, %s)",
            (name, email, message),
        )
        conn.commit()
        cursor.close()
        conn.close()
        flash("Thanks! Your submission was saved successfully.", "success")
    except Error as e:
        flash(f"Database error: {e}", "error")

    return redirect(url_for("index"))


@app.route("/records")
def records():
    """Read and display all stored submissions."""
    rows = []
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM submissions ORDER BY created_at DESC")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except Error as e:
        flash(f"Database error: {e}", "error")

    return render_template("records.html", records=rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
