from flask import Flask

app = Flask(__name__)

#setting up URL!
@app.route("/")

def somename ():
    return "Hello world!"
