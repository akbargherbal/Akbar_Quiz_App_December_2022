from flask import Flask, render_template, request, redirect, url_for
from flask_cors import cross_origin

from utilities import get_datetime_now, get_quiz_collection
import pandas as pd
from zipfile import ZipFile
import os


quiz_repo = os.listdir('quiz_repo')
quiz_repo_dict = {int(i.split('_')[0]):f'quiz_repo/{i}' for i in quiz_repo if i.endswith('.zip')}

path_to_quiz_collection = 'quiz_repo/01_EN_NOUN_AV_16NOV2022.zip'
zf = ZipFile(path_to_quiz_collection)

# Add condition to read only untried quizzes.
quiz_path = get_quiz_collection(path_to_quiz_collection)
quiz_path = quiz_path[0]
zf = ZipFile(path_to_quiz_collection)


quiz_set_from_flask =  pd.read_csv(zf.open(quiz_path), encoding='utf-8').to_dict(orient = 'records')
quiz_name_from_flask = quiz_path

app = Flask(__name__)
app.static_folder = 'static'



@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            print(f'{request.form.to_dict()}', flush=True)
            if 'request_quiz_name' in request.form.to_dict():
                quiz_id = int(request.form.get('request_quiz_name'))
                quiz_path = quiz_repo_dict[quiz_id]
                zf = ZipFile(quiz_path)
                quiz_path = get_quiz_collection(quiz_path)
                quiz_path = quiz_path[0] # Add condition to read only untried quizzes.

                print(f'Quiz_Path: {quiz_path}', quiz_path, flush=True)
        
                quiz_set_from_flask =  pd.read_csv(zf.open(quiz_path), encoding='utf-8').to_dict(orient = 'records')
                quiz_name_from_flask = quiz_path

                kwargs = {'quiz_set_from_flask':quiz_set_from_flask, 
                        'quiz_name_from_flask':quiz_name_from_flask}
                return render_template('quiz.html', **kwargs)
            else:
                print(f'ELSE STATEMENT IN HOME PAGE:', flush=True)
                print('_'*100, flush=True)
                return render_template('home.html')

        except Exception as e:
            print(f'Error: {e}', flush=True)
            print(f'Exception Occured! Redirecting to Home Page:', flush=True)
            print('#'*100, flush=True)
            return render_template('home.html')





@app.route('/quiz' , methods=['POST', 'GET'])
@cross_origin()
def quiz():
    print('Entering QUIZ PAGE!!!', flush=True)
    if request.method == 'GET':
        return render_template('quiz.html')
    
    else:
        try:
            if 'quiz_result' in request.form.to_dict():
                print(f'''
    Quiz Result in Request Form Are Being Printed:
    {request.form.to_dict()}
    ''', flush=True)
                return render_template('home.html')

            else:
                print(f'ELSE STATEMENT IN QUIZ PAGE:', flush=True)
                print('_'*100, flush=True)
                return render_template('home.html')

        except Exception as e:
            print(f'Error: {e}', flush=True)
            print(f'Exception Occured in Quiz Page! Redirecting to Home Page:', flush=True)
            print('#'*100, flush=True)
            return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
