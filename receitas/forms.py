from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from models import Ingrediente


def ingredientes_query():
    return Ingrediente.query


class ReceitaForm(FlaskForm):

    nome = StringField('Nome da Receita', validators=[DataRequired()])
    autor = StringField('Autor da Receita', validators=[DataRequired()])
    modo_preparo = TextAreaField('Modo de Preparo', validators=[DataRequired()])
    ingredientes = QuerySelectMultipleField(query_factory=ingredientes_query, allow_blank=True)
    publicar = SubmitField('Publicar Receita')
