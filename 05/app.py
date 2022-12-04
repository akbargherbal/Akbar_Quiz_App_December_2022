from flask import Flask, render_template, request, redirect, url_for
import json 
app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():   
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        with open('file.json', 'w') as f:
            json.dump(request.form, f)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

