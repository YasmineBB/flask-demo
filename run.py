import os
import json
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About Us", company=data)


@app.route("/glossary")
def glossary():
    return render_template("glossary.html", page_title="Glossary")


@app.route("/wines")
def wines():
    return render_template("wines.html")


@app.route("/wines-orange")
def winesOrange():
    return render_template("wines-orange.html")


@app.route("/wines-white")
def winesWhite():
    return render_template("wines-white.html")


@app.route("/wines-red")
def winesRed():
    return render_template("wines-red.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )