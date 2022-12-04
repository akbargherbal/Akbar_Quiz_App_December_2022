from flask import Flask, render_template, request, redirect, url_for
import json 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.static_folder = 'static'

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('file.json', 'w') as f:
            json.dump(request.form, f)
        return redirect(url_for('data'))
    else:
        return render_template('index.html')


@app.route('/data', methods=['POST', 'GET'])
def data():
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, use_debugger=True)

