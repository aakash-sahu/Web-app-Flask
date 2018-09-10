#Create template directory in project folder
#create home.html and so on.
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h2>Hello World!</h2>"
	
@app.route("/about")
def about():
    return "<h2>About page</h2>"	
	
#With following module, run the file directly in python using 'Python filename.py>	
if __name__ == '__main__':
	app.run(debug=True)
	
	
	
#On windows - set FLASK_APP = <file name>
#for debug - set FLASK_DEBUG = 1	
#flask run