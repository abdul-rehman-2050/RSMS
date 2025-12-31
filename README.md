 
# Repair Shop Management System

A lightweight, budget-friendly **repair shop management system** built with Python Flask and TailwindCSS.  
This project is a live build-in-public, aimed at small or mid-size repair shops looking for a practical solution to manage jobs, customers, and invoices — with optional AI-powered invoice OCR.

 

## Features

- **Landing Page** – TailwindCSS-based, responsive and clean.
- **Authentication** – Simple login flow with SQLite database.
- **Job & Customer Tracking** – Placeholder for managing repair jobs and customer records.
- **Invoice OCR (Optional)** – Upload invoices and extract data automatically.
- **Small Budget Friendly** – Lightweight and easy to extend.

---

## Project Structure

```

repair_app/
│
├─ app/
│   ├─ **init**.py           # app factory
│   ├─ config.py             # configuration
│   ├─ extensions.py         # db instance
│   ├─ models.py             # User model
│   ├─ routes/
│   │   ├─ **init**.py
│   │   ├─ main.py           # landing page routes
│   │   └─ auth.py           # login routes
│   └─ templates/
│       ├─ base.html
│       ├─ index.html
│       └─ login.html
├─ run.py                    # entry point
└─ requirements.txt

````

---

## Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/repair-shop-system.git
cd repair-shop-system
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python run.py
```

5. **Visit in browser**

```
http://127.0.0.1:5000/
```

* `/` → Landing page
* `/auth/login` → Login page

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** SQLite
* **Frontend:** TailwindCSS
* **Extras:** Blueprint structure, modular and easy to extend

---

## Contributing / Freelance Use

This project is structured for **small-business usage** and is still in progress.
If you’re a small repair shop owner and want a **custom version**, feel free to contact via email in the landing page.

Contributions are welcome! Please fork and create pull requests for improvements, especially around authentication, dashboard, and OCR modules.

 
