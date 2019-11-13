from flask import Flask
from flask import render_template
import get_transcript_info as result

app = Flask(__name__)

@app.route("/")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/results")
def show_transcript_results():
    results = result.get_transcript_info()
    return render_template("show_transcript_results.html", results = results)
