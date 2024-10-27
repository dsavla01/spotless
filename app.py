from flask import Flask, render_template, request, g
import sqlite3
import os
from __init__ import create_app  # Import create_app from init.py

app = create_app()  # Call create_app to initialize the app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heatmap")
def heatmap():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT latitude, longitude, rating, response FROM surveyInfo;") #select all columns initially
    survey_data = [
        {
            "latitude": row["latitude"],  #extract info
            "longitude": row["longitude"],
            "rating": row["rating"],
            "response": row["response"]
        } for row in cursor.fetchall()
        #each row fetched from the database is rep. as a dictionary  
        # keys correspond to column names
    ]
    return render_template("heatmap.html", survey_data=survey_data)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(
            app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        db.row_factory = sqlite3.Row
    return db

@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        longitude = request.form.get("longitude")
        latitude = request.form.get("latitude")  
        response = request.form.get("response")  
        rating = request.form.get("rating")  

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO surveyInfo (longitude, latitude, response, rating) VALUES (?, ?, ?, ?)",
            (longitude, latitude, response, rating),
        )
        db.commit()
        
        return render_template("survey.html", message="Response recorded! Return to homepage, view our heat map that tracks pollution, or check out clean up opportunities near you.")

    return render_template("survey.html")

if __name__ == "__main__":
    app.run(debug=True)