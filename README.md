# Python Developer Assignment

## Overview

This project was completed as part of a Python Developer assignment.  
It demonstrates core Python programming skills including:

- Data Processing (CSV handling)
- REST API Integration
- Object-Oriented Programming (OOP)
- SQL Query Writing
- Debugging and Code Fixing

The implementation focuses on clean structure, readability, and proper error handling.

---

## Project Structure
```
project/
│
├── dataset/
│ └── employees.csv
│
├── tasks/
│ ├── task1_data_processing.py
│ ├── task2_api_integration.py
│ ├── task3_library_management_system.py
│ ├── task4_sql_queries.sql
│ └── task5_debugging.py
│
└── README.md
└── custom_exception.py
└── requirements.txt
```


---

## Task 1: Employee Data Processing

- Read employee data from CSV
- Count total employees
- Calculate average salary by department
- Identify department with highest average salary
- Find employees joined in 2023
- Export filtered results
  
---

## Task 2: REST API Integration

API Used:  
https://jsonplaceholder.typicode.com/posts

Features:
- Fetch all posts
- Display total posts
- Filter posts by user ID
- Find longest post title
- Create new post using POST request
- Implement retry logic
- Implement 5-minute file-based caching

---

## Task 3: Library Management System (OOP)

### Classes Implemented

### Book
- title
- author
- isbn
- available
- mark_borrowed()
- mark_returned()

### Library
- add_book()
- remove_book()
- find_book()
- borrow_book()
- return_book()
- display_available_books()
  
---

## Task 4: SQL Queries

Wrote SQL queries for:

- Fetch all employees
- Count employees
- Average salary by department
- Highest average salary department
- Highest paid employee
- Employees joined in 2023
- Count employees per department

---

## Task 5: Debugging & Code Fixing

Identified and fixed issues including:

- Improper file handling
- Type conversion errors
- Dictionary initialization bugs
- Date parsing errors
- Incorrect comparisons
- Infinite recursion

---

## How to Run
```
From project root:

```
python -m venv env1
```

```
env1\scripts\activate
```

```
pip install -r requirements.txt
```
#### task files are inside root/tasks/ Folder

```
python -m tasks.task_file_name
```
```
