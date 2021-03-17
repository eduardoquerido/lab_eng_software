import os
from flask import (
    Flask, request, jsonify,
    render_template, redirect,
    url_for
)
from flask_sqlalchemy import SQLAlchemy
from models import Receita

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def home():
    receitas = Receita.query.all()
    return render_template("home.html", receitas=receitas)


@app.route("/receita/<id_>")
def get_receita_by_id(id_):
    try:
        receita = Receita.query.filter_by(id=id_).first()
    except Exception as e:
        return(str(e))

    return render_template("receita.html", receita=receita)


@app.route("/add/receita", methods=['GET', 'POST'])
def add_receita_form():
    if request.method == 'POST':
        nome = request.form.get('nome')
        autor = request.form.get('autor')
        publicado_em = request.form.get('publicado_em')
        try:
            receita = Receita(
                nome=nome,
                autor=autor,
                publicado_em=publicado_em
            )
            db.session.add(receita)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            return(str(e))
    return render_template("adicionar_receita_form.html")


if __name__ == '__main__':
    app.run()

