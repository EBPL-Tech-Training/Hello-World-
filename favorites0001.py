#favorites0001.py
import csv

from cs50 import SQL

open("shows.db", "w").close()
db = SQL("sqlite:///Shows.db")

db.execute("CREATE TABLE shows1 (id INTEGER, title TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE genres1 (show_id INTEGER, genre TEXT, FOREIGN KEY(show_id) REFERENCES shows1(id))")

with open("Favorite TV Shows - Form Responses 1.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row["title"].strip().upper()

        id = db.execute("INSERT INTO shows1 (title) VALUES(?)", title)

        for genre in row["genres"].split(", "):
            db.execute("INSERT INTO genres1 (show_id, genre) VALUES(?, ?)", id, genre)