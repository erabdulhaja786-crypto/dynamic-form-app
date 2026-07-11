# Dynamic Form Application with Database Storage

A dynamic web application that captures user input through an HTML form and stores submitted data persistently in a MySQL database. Built with Flask, Bootstrap, and vanilla JavaScript, it implements front-end validation and back-end logic to handle form submission, insertion, and retrieval of records — the core CRUD (Create, Read) concepts and the foundation of full-stack development.

## Features

- Responsive HTML form styled with Bootstrap 5
- Front-end (JavaScript) validation for required fields and email format
- Back-end (Flask) validation as a safety net against invalid or malicious input
- MySQL database integration for persistent storage
- A records page to view all previously submitted entries (Read)

## Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend:** Python (Flask)
- **Database:** MySQL

## Project Structure

```
dynamic-form-app/
├── app.py                 # Flask application and routes
├── schema.sql              # MySQL table schema
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html           # Form page
│   └── records.html         # Records/read page
└── static/
    ├── css/style.css
    └── js/validate.js       # Front-end validation logic
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/dynamic-form-app.git
cd dynamic-form-app
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up MySQL

Create the database using the provided schema:

```bash
mysql -u root -p < schema.sql
```

Or simply run the app — `init_db()` in `app.py` will create the table automatically if it doesn't exist (the database itself must exist first).

### 4. Configure environment variables

```bash
export DB_HOST=localhost
export DB_USER=root
export DB_PASSWORD=yourpassword
export DB_NAME=dynamic_form_db
```

### 5. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## How It Works

1. The user fills out the form on the home page.
2. JavaScript validates the fields client-side before allowing submission.
3. On submit, the form POSTs to `/submit`, where Flask re-validates the data server-side.
4. Valid data is inserted into the `submissions` table in MySQL.
5. Visiting `/records` reads and displays all stored submissions in a table.

## Author

Abdul Rahman
