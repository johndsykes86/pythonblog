from flask import Flask

app = Flask(__name__)

#setting up URL!
@app.route("/")

def index ():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/contact')
def contact():
    return app.send_static_file('contact.html')
