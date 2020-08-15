from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
import os
import tempfile
from model.model import prediction

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homePage():
	if request.method == 'GET':
		return render_template('home-page.html')

@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		pic_file = request.files['file']
		pic_name = secure_filename(pic_file.filename)
		pic_path = os.path.join(tempfile.gettempdir(), pic_name)
		pic_file.save(pic_path)

		output = prediction(pic_path)

		os.remove(pic_path)

		return redirect(url_for('output', output = output))

@app.route('/output', methods=['GET'])
def output():
	if request.method == 'GET':
		output = request.args.get('output')

		return render_template('output.html', output = output)


if __name__ == '__main__':
	app.run(debug = True)