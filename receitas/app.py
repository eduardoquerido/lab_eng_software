import os
import datetime
from flask import (
    Flask, request, jsonify,
    render_template, redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

'''
    O modelo está sendo importado abaixo para não entrar em conflito de
    com importação circular com a importação do banco de dados no
    módulo de "manage.py"
'''

from models import Receita, Ingrediente
from forms import ReceitaForm


@app.route("/")
def home():
    receitas = Receita.query.all()
    return render_template("home.html", receitas=receitas)


@app.route("/ingredientes")
def lista_ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template("ingrediente_list.html", ingredientes=ingredientes)


@app.route("/receita/<id_>")
def get_receita_by_id(id_):
    try:
        receita = Receita.query.filter_by(id=id_).first()

    except Exception as e:
        return(str(e))

    return render_template("receita.html", receita=receita)


@app.route("/add/receita", methods=['GET', 'POST'])
def add_receita_form():
    form = ReceitaForm(request.form)

    if form.validate():
        nome = form.nome.data
        autor = form.autor.data
        ingredientes = form.ingredientes.data
        modo_preparo = form.modo_preparo.data
        publicado_em = datetime.datetime.now()

        try:
            receita = Receita(
                nome=nome,
                autor=autor,
                publicado_em=publicado_em,
                modo_preparo=modo_preparo
            )

            if ingredientes:
                for ing in ingredientes:
                    receita.ingredientes.append(ing)

            db.session.add(receita)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            return(str(e))

    return render_template("adicionar_receita_form.html", form=form)


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
            return redirect(url_for('lista_ingredientes'))
        except Exception:
            return render_template("adicionar_ingrediente_form.html")
    return render_template("adicionar_ingrediente_form.html")


if __name__ == '__main__':
    app.run()
