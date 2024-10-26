from flask import Flask, render_template
app = Flask(__name__, template_folder = "templates")

import sqlite3

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/heatmap")
def heatmap():
    return render_template("heatmap.html")

DATABASE = 'survey.db'
app.config['DATABASE'] = DATABASE

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf-8'))

@app.route("/survey", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        longitude = request.form.get("longitude")
        latitude = request.form.get("latitude")  
        response = request.form.get("response")  
        rating = request.form.get("rating")  


        # print(email)
        # print(password)
        db = get_db()
        cursor = db.cursor()

    cursor.execute(
            "INSERT INTO userinfo (longitude, latitude, response, rating) VALUES (?, ?, ?, ?)",
            (longitude, latitude, response, rating),
        )
    db.commit()



if __name__ == "__main__":
    app.run(debug=True)