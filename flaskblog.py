from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



###from flask import Flask, render_template
##app = Flask(__name__,
            template_folder="templates")

###@app.route("/")
###def home():
## return render_template('index.html',