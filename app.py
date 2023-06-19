from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
                           
@app.route('/skills')
def skills():
    return render_template('skills.html')
                         