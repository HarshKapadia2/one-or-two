from flask import Flask, render_template, url_for, request, redirect, flash, session
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
import tempfile
from model.model import prediction

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error-404.html'), 404

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
		output_list = output.split(' ')

		# weird model output issue handled
		if output_list[1] == '':
			output_list.pop(1)

		output_1 = float(output_list[0][2:] or 0)
		output_2 = float(output_list[1][:-2] or 0)

		# clearing previous session to remove any residual flash messages
		session.clear()

		return render_template(
			'output.html',
			output_1 = {
				'percentage': '{:.4f}'.format(round(100 * output_1, 4)),
				'display_class': 'right' if output_1 > output_2 else 'wrong'
			},
			output_2 = {
				'percentage': '{:.4f}'.format(round(100 * output_2, 4)),
				'display_class': 'right' if output_2 > output_1 else 'wrong'
			}
		)


if __name__ == '__main__':
	app.run()