from flask import Flask, render_template, url_for, request, redirect, flash, session
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
import tempfile
from model.model import prediction

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET'])
def homePage():
	if request.method == 'GET':
		return render_template('home-page.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		# check if the request has the file part
		if 'file' not in request.files:
			flash('NOTE: No file received by the server. Please select a file...')
			return redirect('/')

		pic_file = request.files['file']

		# check if the user has chosen a file
		if pic_file.filename == '':
			flash('NOTE: No file selected. Please select a file...')
			return redirect('/')

		pic_name = secure_filename(pic_file.filename)
		pic_extension = pic_name.split('.')[1].lower()

		# check if the uploaded file is an image of the following types
		if pic_extension not in ('png', 'jpg', 'jpeg'):
			flash('NOTE: Wrong file type selected. Only png, jpg and jpeg files are accepted...')
			return redirect('/')
		
		pic_path = os.path.join(tempfile.gettempdir(), pic_name)
		pic_file.save(pic_path)

		output = prediction(pic_path)

		os.remove(pic_path)

		return redirect(url_for('output', output = output))

@app.route('/output', methods=['GET'])
def output():
	if request.method == 'GET':
		output = request.args.get('output')
		session.clear()

		return render_template('output.html', output = output)


if __name__ == '__main__':
	app.run()