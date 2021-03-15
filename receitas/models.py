from app import db


class Receita(db.Model):
    __tablename__ = 'receita'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    autor = db.Column(db.String())
    publicado_em = db.Column(db.String())

    def __init__(self, nome, autor, publicado_em):
        self.nome = nome
        self.autor = autor
        self.publicado_em = publicado_em

    def __repr__(self):
        return '{}'.format(self.nome)

    def serialize(self):
        return {
            'id': self.id, 
            'nome': self.nome,
            'autor': self.autor,
            'publicado_em':self.publicado_em
        }
