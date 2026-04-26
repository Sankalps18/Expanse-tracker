import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "spendly.db"


def get_db():
    """
    Opens a connection to the SQLite database.
    Sets row_factory for dict-like access and enables foreign keys.
    Returns the connection.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """
    Creates the users and expenses tables if they don't exist.
    Safe to call multiple times.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)

    # Create expenses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """
    Inserts sample data for development.
    Checks for existing data to prevent duplicates.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Check if users table already has data
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    if count > 0:
        conn.close()
        return  # Data already exists, skip seeding

    # Create demo user
    demo_password_hash = generate_password_hash("demo123")
    cursor.execute("""
        INSERT INTO users (name, email, password_hash)
        VALUES (?, ?, ?)
    """, ("Demo User", "demo@spendly.com", demo_password_hash))

    # Get the demo user's ID
    cursor.execute("SELECT id FROM users WHERE email = ?", ("demo@spendly.com",))
    user_id = cursor.fetchone()[0]

    # Insert 8 sample expenses across different categories
    # Using dates from current month (April 2026)
    expenses = [
        (user_id, 450.00, "Food", "2026-04-01", "Grocery shopping at Walmart"),
        (user_id, 120.50, "Transport", "2026-04-03", "Monthly bus pass"),
        (user_id, 2500.00, "Bills", "2026-04-05", "Electricity bill"),
        (user_id, 350.00, "Health", "2026-04-08", "Pharmacy - prescription"),
        (user_id, 800.00, "Entertainment", "2026-04-10", "Movie tickets and dinner"),
        (user_id, 1200.00, "Shopping", "2026-04-12", "New shoes and clothes"),
        (user_id, 65.00, "Food", "2026-04-15", "Lunch at restaurant"),
        (user_id, 500.00, "Other", "2026-04-18", "Gift for friend's birthday"),
    ]

    cursor.executemany("""
        INSERT INTO expenses (user_id, amount, category, date, description)
        VALUES (?, ?, ?, ?, ?)
    """, expenses)

    conn.commit()
    conn.close()
