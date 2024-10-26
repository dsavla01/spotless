import os
from flask import Flask, g
import sqlite3

def get_db(app):
    if 'db' not in g:
        # Connect to the SQLite database
        g.db = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db(app):
    """Initialize the database using the schema.sql file."""
    with app.app_context():
        db = get_db(app)
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf-8'))

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'survey.db')  # Updated to match your app
    )

    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    # Set up the database functions
    app.teardown_appcontext(close_db)

    # Initialize the database
    init_db(app)

    return app
