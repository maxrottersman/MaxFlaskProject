from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Max World!'

@app.route('/bootstrap')
def welcome():
    return render_template('base.html')  # render a templat

@app.route('/extendedbase')
def extendedbase():
    return render_template('page_extended_from_base.html')  # render a templat