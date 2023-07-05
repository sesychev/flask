import os
from flask import Flask, render_template, json, current_app
from data import data_fake, titles

app = Flask(__name__)

# static/data/test_data.json
education = os.path.join(app.static_folder, 'data', 'education.json')
experience = os.path.join(app.static_folder, 'data', 'experience.json')
publications = os.path.join(app.static_folder, 'data', 'publications.json')

with open(education) as education_file:
    data_education = json.load(education_file)

with open(experience) as experience_file:
    data_experience = json.load(experience_file)

with open(publications) as publications_file:
    data_publications = json.load(publications_file)
# print(data)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/education')
def education():
    return render_template('education.html', data=data_education)


@app.route('/experience')
def experience():
    return render_template('experience.html', data=data_experience)


@app.route('/publications')
def publications():
    return render_template('publications.html', data=data_publications)


@app.route('/table')
def table():
    return render_template('table.html', data=data_fake, titles=titles)


@app.route('/ifc')
def ifc():
    return render_template('ifc.html', data=data_fake)


if __name__ == "__main__":
    pass

'''
#@app.route('/about')
#def about():
#    return render_template('about.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')
                           
@app.route('/skills')
def skills():
    return render_template('skills.html')
'''
