import os
from flask_paginate import Pagination, get_page_args
from flask import Flask, render_template, json, request

from modules.data import data_fake, titles
from modules.regress import reg

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
@app.route('/about')
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
    total = len(data_fake)
    page, per_page, offset = get_page_args(
        page_parametr="page",
        per_page_parmeter="per_page")
    pagination = Pagination(page=page, total=total)
    return render_template('table.html', data=data_fake[offset: offset+per_page], titles=titles, pagination=pagination)


@app.route('/ifc')
def ifc():
    return render_template('ifc.html', data=data_fake)


@app.route('/progress', methods=('GET', 'POST'))
def progress():
    if request.method == 'POST':
        data = reg()
        return render_template('progress.html', data=data)
    # print(data)
    return render_template('progress.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
