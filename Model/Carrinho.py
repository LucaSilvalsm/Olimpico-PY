from Model import db

class Carrinho(db.Model):
    __tablename__ = 'carrinho'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nome_produto = db.Column(db.String(200))
    imagem_produto = db.Column(db.String(200))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    quantidade = db.Column(db.Integer)
    observacao = db.Column(db.Text)
    preco_total = db.Column(db.Numeric(10, 2))
    
