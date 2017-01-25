from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():

	return "welcome! this is your first webapp program"
if __name__=="__main__":
	app.run()
