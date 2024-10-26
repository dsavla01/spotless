import os
from flask import Flask, g
import sqlite3

def get_db():
    if 'db' not in g:
        # Connect to the SQLite database in the instance folder
        g.db = sqlite3.connect(
            os.path.join(app.instance_path, 'my_database.db')
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'my_database.db')
    )

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Set up the database functions
    app.teardown_appcontext(close_db)

    return app
