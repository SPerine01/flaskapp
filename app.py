from flask import Flask, render_template
from flask sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 
from data import Articles
# render_template brings in the the different pages from the template folder

app = Flask(__name__)

db = SQLAlchemy(app)

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

@app.route('/article/<string:id>/')
def article(id):
	return render_template('article.html', id = id)
# string type passing in the parameter of id and then its passed into the function

if __name__ == '__main__':
	app.run(debug=True)
