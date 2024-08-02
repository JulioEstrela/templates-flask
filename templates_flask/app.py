from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_home_page():
    return render_template('home.html')

@app.route('/contato')
def render_contato_page():
    return render_template('contato.html')

@app.route('/produtos')
def render_produtos_page():
    return render_template('produtos.html')

@app.route('/termos-de-uso')
def render_termos_de_uso_page():
    return render_template('termos-de-uso.html')

@app.route('/politica-de-privacidade')
def render_politica_de_privacidade_page():
    return render_template('politica-de-privacidade.html')

@app.route('/como-usar')
def render_como_usar_page():
    return render_template('como-usar.html')