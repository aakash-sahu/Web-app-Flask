from flask import Flask, render_template, url_for

app = Flask(__name__)

posts =[
	{
		'author': 'Aakash Sahu',
		'title': 'First blog post',
		'content': 'First post content using Flask',
		'date': '17th July 2018'
	},
	{
		'author': 'John Doe',
		'title': 'Another blog post',
		'content': 'Second post content using Flask',
		'date': '18th July 2018'
	}	
	]

@app.route("/")
@app.route("/home")
def Home():
	return render_template('home.html', posts = posts)
	
@app.route("/about")
def about():
	return render_template('about.html', title = 'About')	

if __name__ == '__main__':
	app.run(debug=True)	