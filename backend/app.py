
from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/reflected_xss')
def reflected_xss():
    return render_template('reflected_xss.html')

@app.route('/stored_xss')
def stored_xss():
    return render_template('stored_xss.html')

@app.route('/dom_xss')
def dom_xss():
    return render_template('dom_xss.html')


if __name__ == '__main__':
    app.run(debug=True)
