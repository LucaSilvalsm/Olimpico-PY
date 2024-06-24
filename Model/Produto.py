from Model import db

class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String(200))
    tipo_produto = db.Column(db.String(200))
    tamanho = db.Column(db.String(200))
    ingrediente = db.Column(db.String(200))
    preco = db.Column(db.Numeric(10, 2))
    descricao = db.Column(db.Text)
    imagem = db.Column(db.String(250))
    
