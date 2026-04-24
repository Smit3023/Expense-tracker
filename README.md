# 💸 Expense Tracker

> A lightweight full-stack web application to **log, manage, and summarize daily expenses** — built with **Django**. Users can add expenses with categories and dates, edit or delete them, and view a monthly spending summary.

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Application Flow](#-application-flow)
- [Database Models](#-database-models)
- [Getting Started](#-getting-started)
- [URL Routes](#-url-routes)

---

## 📖 About the Project

Expense Tracker is a **CRUD-based web app** that helps users keep track of where their money goes. It supports organizing expenses by category, filtering by month, and generating a total spending summary — all through a simple web interface backed by Django.

This project demonstrates core Django skills including **model design, form handling, ORM queries, URL routing, and template rendering**.

---

## 🧰 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Backend      | Python, Django 6.0             |
| Database     | SQLite                         |
| Frontend     | Django Templates, HTML         |
| ORM          | Django ORM with aggregation    |

---

## ✅ Features

- **Add Expense** — Log description, amount, date, and category
- **View All Expenses** — See all expenses in a table
- **Edit Expense** — Update any existing expense entry
- **Delete Expense** — Remove an expense by ID
- **Monthly Summary** — Filter expenses by month and view total spend
- **Category Management** — Expenses are linked to reusable categories

---

## 📁 Project Structure

```
Expense-tracker-main/
│
└── config/                       # Django root
    ├── config/                   # Project settings
    │   ├── settings.py           # App configuration
    │   ├── urls.py               # Root URL routing
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── expenses/                 # Main Django app
    │   ├── models.py             # Expense & Category models
    │   ├── views.py              # CRUD + summary views
    │   ├── urls.py               # URL patterns
    │   ├── admin.py              # Admin panel setup
    │   └── templates/
    │       └── expenses/
    │           ├── list.html     # All expenses table
    │           ├── add.html      # Add expense form
    │           ├── edit.html     # Edit expense form
    │           └── summary.html  # Monthly total view
    │
    ├── manage.py
    └── db.sqlite3                # SQLite database
```

---

## 🔄 Application Flow

```
Home (Expense List)
   │
   ├──▶ Add Expense
   │        │
   │        └──▶ Fill form (description, amount, date, category)
   │                  │
   │                  └──▶ Saved to DB ──▶ Redirect to Expense List
   │
   ├──▶ Edit Expense
   │        │
   │        └──▶ Pre-filled form ──▶ Save changes ──▶ Redirect to Expense List
   │
   ├──▶ Delete Expense
   │        │
   │        └──▶ Expense deleted ──▶ Redirect to Expense List
   │
   └──▶ Monthly Summary
            │
            └──▶ Enter month number (1–12)
                      │
                      └──▶ Filtered expenses ──▶ Show total amount
```

---

## 🗄️ Database Models

### `Category`

| Field  | Type         | Description              |
|--------|--------------|--------------------------|
| `id`   | AutoField    | Primary key              |
| `name` | CharField    | Category name (e.g., Food, Travel) |

---

### `Expense`

| Field         | Type        | Description                         |
|---------------|-------------|-------------------------------------|
| `id`          | AutoField   | Primary key                         |
| `description` | CharField   | Short label for the expense         |
| `amount`      | FloatField  | Expense amount                      |
| `date`        | DateField   | Date of the expense                 |
| `category`    | ForeignKey  | Linked to `Category` model          |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker/config

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Apply migrations
python manage.py migrate

# 5. (Optional) Create a superuser for admin access
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit **http://127.0.0.1:8000** in your browser.

---

## 🌐 URL Routes

| URL                    | View              | Description                    |
|------------------------|-------------------|--------------------------------|
| `/`                    | `expense_list`    | View all expenses              |
| `/add/`                | `add_expense`     | Add a new expense              |
| `/edit/<id>/`          | `edit_expense`    | Edit an existing expense       |
| `/delete/<id>/`        | `delete_expense`  | Delete an expense              |
| `/summary/?month=<n>`  | `monthly_summary` | View total spend for a month   |

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
