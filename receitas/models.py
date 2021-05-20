from app import db

receita_ingrediente = db.Table('receita_ingrediente',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True),
    db.Column('quantidade', db.Integer)
)


class Receita(db.Model):
    __tablename__ = 'receita'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    autor = db.Column(db.String(255))
    publicado_em = db.Column(db.DateTime, nullable=False)
    modo_preparo = db.Column(db.UnicodeText(500))
    ingredientes = db.relationship(
        'Ingrediente', secondary=receita_ingrediente, lazy='subquery',
        backref=db.backref('receita', lazy=True)
    )

    def __init__(self, nome, autor, publicado_em, modo_preparo):
        self.nome = nome
        self.autor = autor
        self.publicado_em = publicado_em
        self.modo_preparo = modo_preparo

    def __repr__(self):
        return '{}'.format(self.nome)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'autor': self.autor,
            'publicado_em': self.publicado_em
        }


class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=True)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return '{}'.format(self.nome)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
        }
