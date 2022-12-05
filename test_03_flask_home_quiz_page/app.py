from flask import Flask, render_template, request, redirect, url_for
from flask_cors import cross_origin
import pandas as pd
from datetime import datetime



app = Flask(__name__)



@app.route('/home' , methods=['GET', 'POST'])
@app.route('/' , methods=['GET', 'POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        time_now =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        asked_for = request.form.get('quiz_type')
        asked_for = f'{asked_for} done in python @ {time_now}'
        print(f'Asked for: {asked_for}', flush=True)
        return render_template('quiz.html', asked_for=asked_for)

    return render_template('home.html')


@app.route('/quiz', methods=['POST', 'GET'])
@cross_origin()
def quiz():
    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)