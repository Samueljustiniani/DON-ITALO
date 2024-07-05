from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vestimentas')
def vestimentas():
    return render_template('vestimentas.html')

@app.route('/tecnologias')
def tecnologias():
    return render_template('tecnologias.html')

@app.route('/decoraciones')
def decoraciones():
    return render_template('decoraciones.html')
