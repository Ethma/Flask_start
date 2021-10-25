from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Testß'

@app.route('/<page>/')
def route(page):
	return page
if __name__ == '__main__':
	app.run()