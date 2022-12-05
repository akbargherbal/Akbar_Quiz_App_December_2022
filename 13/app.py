from flask import Flask, render_template, request, redirect, url_for
from flask_cors import cross_origin
import pandas as pd
from utilities import open_zip_csv

quiz_set_from_flask =  open_zip_csv(0,0).to_dict(orient = 'records')

quiz_name_from_flask = 'VERB_QUIZ_004'

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/quiz' , methods=['GET', 'POST'])
@cross_origin()
def quiz():
    if request.method == 'POST': # Posting Quiz Results!
        print('Entering Post!!!', flush=True)
        result = request.values
        result = result.to_dict()
        print(f'{result}', flush=True)
        
        with open('data.txt', '+a', encoding='utf-8') as f:
            for v in result.values():
                f.write(f'{v} ')
            f.write('\n')
        try:
            quiz_name = request.form.get('quiz_name')
            print(f'Quiz Name: {quiz_name}', flush=True)
        except Exception as e:
            print(f'Error: {e}', flush=True)
    kwargs = {'quiz_set_from_flask': quiz_set_from_flask,
            'quiz_name_from_flask': quiz_name_from_flask}
    
    return render_template('quiz.html', **kwargs)


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    print('Entering HOME PAGE!!!', flush=True)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
