import sqlite3
import os

def create_db():
    db_path = os.path.join('instance', 'my_database.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Create an example table (e.g., users table)
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
