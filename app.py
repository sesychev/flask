from flask import Flask, render_template, json, current_app
import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util
import ifcopenshell.util.element
import os
#from ifc_viewer import ifc_viewer

ifc = ifcopenshell.open('static/ifc/____P0-02-070.ifc')

wall = ifc.by_type('IfcBeam')[0]
#print(wall.is_a())
#print(wall.get_info())
#https://wiki.osarch.org/index.php?title=IfcOpenShell_code_examples
#https://linjiarui.net/en/posts/2020-06-15-opensource-bim-tools
#https://trimsh.org/examples.html#quick-start-ipynb
#https://github.com/ifcjs/
#https://github.com/stefkeB/ifcopenshell_examples/tree/main/3D
#https://github.com/stefkeB/ifcopenshell_examples/blob/main/3D/qt3d_minimal.py
#https://github.com/R-Rijnbeek/IFC_WebViewer/tree/master
#https://github.com/AECgeeks/ifc-pipeline/tree/master
#https://blog.skillfactory.ru/kak-napisat-veb-prilozhenie-dlya-demonstratsii-data-science-proekta-na-python/

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

#print(data)

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

@app.route('/ifc')
def ifc():
    return render_template('ifc.html')

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


import random
import sys
from faker import Faker



if __name__ == "__main__":
    pass  
              