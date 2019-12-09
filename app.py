from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import get_transcript_info as result
import recommlett_senti as senti
import predict_ver2 as getpreresult
import os
import urllib.request
from flask import flash, request, redirect
from werkzeug.utils import secure_filename
from forms import DataForm
import csv

DEBUG = True

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

UPLOAD_FOLDER = 'D:\study\BU Grad  Fall 2019\EC601 Product Design ECE\Main Project\EC601-Project-AAS\pdfs'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config.from_object(__name__)
report = []

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")

@app.route("/index")
def index():
	return render_template("index.html")

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
	results_str = 'The recommendation letter sentiment analysis result is: ' + results
	report.append(results_str)
	return render_template("show_recomm_results.html", results = results)

@app.route("/predict", methods=['GET', 'POST'])
def predict():
	form = DataForm()
	if form.validate_on_submit():
		GRE = form.GRE.data
		TOEFL = form.TOEFL.data
		rating = form.rating.data
		SOP = form.SOP.data
		LOR = form.LOR.data
		CGPA = form.CGPA.data
		Research = form.Research.data
		fieldnames = ['GRE', 'TOEFL', 'rating', 'SOP', 'LOR', 'CGPA', 'Research']
		with open('admission_data.csv','w') as inFile:
			writer = csv.DictWriter(inFile, fieldnames=fieldnames)
			writer.writerow({'GRE', 'TOEFL', 'rating', 'SOP', 'LOR', 'CGPA', 'Research'})
			writer.writerow({'GRE': GRE, 'TOEFL': TOEFL, 'rating': rating, 'SOP': SOP, 'LOR': LOR, 'CGPA': CGPA, 'Research': Research})
		results = getpreresult.predict()
		return render_template("predict_result.html", results = results)
	else:
		return render_template("predict.html", form = form)
	return render_template("predict.html", form = form)

@app.route("/predict_result", methods=['GET', 'POST'])
def predict_result():
	if request.method == 'POST':
		GRE = request.form['GRE']
		TOEFL = request.form['TOEFL']
		rating = request.form['rating']
		SOP = request.form['SOP']
		LOR = request.form['LOR']
		CGPA = str(float(request.form['CGPA']) / 4 * 10)
		Research = request.form['Research']
		fieldnames = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']
		with open('admission_data.csv','w') as inFile:
			writer = csv.DictWriter(inFile, fieldnames=fieldnames)
			writer.writerow({'GRE Score': 'GRE Score', 'TOEFL Score': 'TOEFL Score', 'University Rating': 'University Rating', 'SOP': SOP, 'LOR': LOR, 'CGPA': CGPA, 'Research': Research})
			writer.writerow({'GRE Score': GRE, 'TOEFL Score': TOEFL, 'University Rating': rating, 'SOP': SOP, 'LOR': LOR, 'CGPA': CGPA, 'Research': Research})
		results = getpreresult.predict()
		results_str = 'The chance of admission is: ' + str(results)
		report.append(results_str)
	return render_template("predict_result.html", results = results)

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

