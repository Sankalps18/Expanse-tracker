# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spendly is a Flask-based expense tracking web application. The app is built as a teaching project with incremental steps for students to implement features.

## Tech Stack

- **Backend**: Flask 3.1.3 with Werkzeug
- **Database**: SQLite (via custom database module)
- **Frontend**: Jinja2 templates with vanilla JavaScript
- **Testing**: pytest with pytest-flask
- **Styling**: Custom CSS with CSS variables

## Commands

```bash
# Run the application
python app.py

# Run tests
pytest

# Run a specific test
pytest -k test_name
```

## Architecture

```
expense-tracker/
├── app.py              # Flask app with routes
├── database/
│   ├── __init__.py     # Package init
│   └── db.py           # Database utilities (get_db, init_db, seed_db)
├── templates/          # Jinja2 HTML templates
├── static/
│   ├── css/           # Stylesheets
│   └── js/            # JavaScript
└── venv/              # Python virtual environment (gitignored)
```

## Key Patterns

- **Database**: The `database/db.py` module provides `get_db()`, `init_db()`, and `seed_db()` functions for SQLite connections with `row_factory` and foreign keys enabled
- **Templates**: All templates extend `base.html` which provides the navbar, footer, and common assets
- **Routes**: Currently implements landing, register, login, terms, and privacy pages; placeholder routes exist for logout, profile, and expense CRUD operations

## Current State

The app has:
- Landing page with hero section and feature cards
- Authentication pages (login/register) - UI only
- Terms and privacy policy pages
- Placeholder routes for expense management features (to be implemented)
- Database module skeleton (to be implemented)
