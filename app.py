from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return "Helow world!"


@app.route('/<name>')
def print_name(name):

	return 'Hi there, {} '.format(name)





if __name__ == '__main__':
	app.run(debug=True)