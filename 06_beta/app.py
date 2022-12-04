from flask import Flask, render_template, request, redirect, url_for, jsonify
import json 
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/index')
@app.route('/' , methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        with open('data.json', '+a') as f:
            json.dump(request.form, f)   
    return render_template('index.html')


@app.route('/data', methods=['GET', 'POST'])
@cross_origin()
def data():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

