import os
from flask import (
    Flask, request, jsonify,
    render_template, redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''
    O modelo está sendo importado abaixo para não entrar em conflito de
    com importação circular com a importação do banco de dados no
    módulo de "manage.py"
'''

from models import Receita, Ingrediente

@app.route("/")
def home():
    # receitas = Receita.query.all()
    receitas = [
        "Bolo de Chocolate",
    ]
    return render_template("home.html", receitas=receitas)


@app.route("/receita/<id_>")
def get_receita_by_id(id_):
    try:
        # receita = Receita.query.filter_by(id=id_).first()
        receita = {
            'id': 1,
            'nome': 'Bolo de Chocolate',
            'autor': 'Eduardo Querido',
            'publicado_em': '19/03/2021',
        }
        ingredientes = {
            'Leite condensado': '1 lata',
            'Leite morno': '1 xícara',
            'Óleo': '1 xícara',
            'Ovo': '3',
            'Farinha de trigo': '100g'
        }
    except Exception as e:
        return(str(e))

    return render_template("receita.html", receita=receita, ingredientes=ingredientes)


@app.route("/add/receita", methods=['GET', 'POST'])
def add_receita_form():
    if request.method == 'POST':
        nome = request.form.get('nome')
        autor = request.form.get('autor')
        publicado_em = request.form.get('publicado_em')
        '''
            As funções estão comentadas pois serão implementadas 
            após a entrega do protótipo navegável
        '''
        # try:
        #     receita = Receita(
        #         nome=nome,
        #         autor=autor,
        #         publicado_em=publicado_em
        #     )
        #     db.session.add(receita)
        #     db.session.commit()
        #     return redirect(url_for('home'))
        # except Exception as e:
        #     return(str(e))
    return render_template("adicionar_receita_form.html")

@app.route("/add/ingrediente", methods=['GET', 'POST'])
def add_ingrediente_form():
    if request.method == 'POST':
        nome = request.form.get('nome')
        try:
            ingrediente = Ingrediente(
                nome=nome,
            )
            db.session.add(ingrediente)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            return(str(e))        
    return render_template("adicionar_ingrediente_form.html")

if __name__ == '__main__':
    app.run()

