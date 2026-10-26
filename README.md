# Student Registration Platform

A Django-based student registration and project showcase application for managing student accounts and project entries.

## Features

- Student registration form
- Student login page
- Project registration form
- Project listing dashboard
- SQLite database for local development

## Tech Stack

- Python 3.13
- Django 6.1.2
- SQLite (development)

## Project Structure

```text
.
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── Procfile
├── runtime.txt
├── env/
├── myproject/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── myapp/
│   └── myproject/
└── ...
```

## Local Setup

1. Open a terminal in the project root.
2. Activate the virtual environment:

```bash
source env/bin/activate
```

On Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
cd myproject
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

Then open:

- http://127.0.0.1:8000/

## Environment Variables

Copy `.env.example` and update the values before deploying:

```bash
cp .env.example .env
```

Example variables:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
DATABASE_URL=sqlite:///db.sqlite3
CSRF_TRUSTED_ORIGINS=https://your-domain.com
```

## Deployment

This project is ready for deployment on services such as Render, Railway, or Heroku.

### Render example

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn myproject.wsgi:application`
- Set environment variables in the dashboard

## Notes

- `env/` is excluded from version control.
- The app uses SQLite by default for local development.
- For production deployments, configure `DATABASE_URL` and a secure secret key.
