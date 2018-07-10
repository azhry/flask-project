from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test/<param>')
def test(param):
	return 'Test %s' % param

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')