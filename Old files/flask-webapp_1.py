from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def Home():
	return "<h1>Hello World! to the home page</h1>"
	
@app.route("/about")
def about():
	return "<h1>Welcome to about page!</h1>"	

if __name__ == '__main__':
	app.run(debug=True)	