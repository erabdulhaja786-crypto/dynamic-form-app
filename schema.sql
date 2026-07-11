-- Run this once to create the database, or let app.py's init_db() create the table for you.

CREATE DATABASE IF NOT EXISTS dynamic_form_db;
USE dynamic_form_db;

CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
