from flask import Flask, render_template
from data import Articles
# render_template brings in the the different pages from the template folder

app = Flask(__name__)

Articles = Articles()

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles = Articles)
	# passing in the data from data.py

if __name__ == '__main__':
	app.run(debug=True)
