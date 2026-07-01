# CCT-Dublin-Catalog

Coursework for the **Diploma in DevOps** at CCT Dublin.

## Overview

A Django REST API application built as part of the DevOps diploma programme. The project demonstrates core backend development concepts including project structure, app architecture, and API design using the Django framework.

## Project Structure

```
CCT-Dublin-Catalog/
├── bookcatalog/        # Core Django project settings and configuration
│   ├── settings.py     # Project settings (installed apps, middleware, database)
│   ├── urls.py         # Root URL configuration
│   └── wsgi.py         # WSGI entry point for deployment
├── api/                # REST API Django app
│   ├── views.py        # API view logic
│   ├── urls.py         # API URL routing
│   └── models.py       # Data models
├── manage.py           # Django management CLI
├── .venv/              # Virtual environment (not tracked in Git)
└── README.md
```

## Tech Stack

- **Python 3** — core language
- **Django** — web framework
- **Django REST Framework** — API layer
- **Git/GitHub** — version control (SSH authentication)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone git@github.com:BarraHarrison/CCT-Dublin-Catalog.git
   cd CCT-Dublin-Catalog
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the development server:
   ```bash
   python3 manage.py runserver
   ```

## Author

Barra Harrison — CCT Dublin, Diploma in DevOps (2026)