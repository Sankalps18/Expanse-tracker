# Spec: Registration

## Overview

This step implements the backend functionality for user registration. Currently the register page exists with a form that POSTs to `/register`, but the route only handles GET requests and renders the template. This step adds the logic to validate input, hash passwords, store users in the database, and handle errors appropriately.

## Depends on

- Step 1: Database setup (completed) — the `users` table and `get_db()` function are available

## Routes

- `GET /register` — Display registration form — public (already exists)
- `POST /register` — Process registration, create user — public (to implement)

## Database changes

No database changes — the `users` table already exists with:
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `name` (TEXT NOT NULL)
- `email` (TEXT UNIQUE NOT NULL)
- `password_hash` (TEXT NOT NULL)
- `created_at` (TEXT DEFAULT datetime('now'))

## Templates

- **Modify:** `templates/register.html` — add `value` attributes to preserve input on error, add success/error message handling with flash messages

## Files to change

- `app.py` — add POST handler for `/register` route
- `templates/register.html` — enhance form with value preservation and flash message display

## Files to create

No new files.

## New dependencies

No new dependencies — Flask and Werkzeug are already available.

## Rules for implementation

- Use parameterized queries only — never interpolate user input into SQL
- Hash passwords with `werkzeug.security.generate_password_hash()`
- Validate email format and check for duplicates before inserting
- Validate password length (minimum 8 characters)
- Use Flask's `flash()` for success/error messages
- Redirect after successful registration (PRG pattern)
- All templates extend `base.html`
- Use CSS variables — never hardcode hex values

## Definition of done

- [ ] GET /register displays the registration form
- [ ] POST /register with valid data creates a new user and redirects to login page
- [ ] POST /register with duplicate email shows error and preserves form data
- [ ] POST /register with weak password (< 8 chars) shows validation error
- [ ] POST /register with invalid email format shows validation error
- [ ] Password is hashed before storing in database
- [ ] Success message displayed after successful registration
- [ ] Form input values preserved on error (except password field)
