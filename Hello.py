from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def vame(name):
	return '<h1>Hello dear %s!</h1><br><u>How are you today??</u>' %name

if __name__ == '__main__':
	app.run(debug=True)
	