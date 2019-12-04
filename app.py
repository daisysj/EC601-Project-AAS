from flask import Flask
from flask import render_template
import get_transcript_info as result
import recommlett_senti as senti
import os
import urllib.request
from flask import flash, request, redirect
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

UPLOAD_FOLDER = 'D:\study\BU Grad  Fall 2019\EC601 Product Design ECE\Main Project\EC601-Project-AAS\pdfs'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
report = []

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

@app.route("/results")
def show_transcript_results():
	results = result.get_transcript_info()
	for i in range(len(results)):
		report.append(results[i])
	return render_template("show_transcript_results.html", results = results)

@app.route("/recommlett")
def recommlett():
    return render_template("recommlett.html")

@app.route("/sentiresults")
def show_recomm_results():
	results = senti.analyze_sentiment()
	report.append(results)
	return render_template("show_recomm_results.html", results = results)

@app.route("/summary")
def summary():
	return render_template("show_summary.html", results = report)

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect(request.url)
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)