from Model import db

class Carrinho(db.Model):
    __tablename__ = 'carrinho'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    nome_produto = db.Column(db.String(50))
    imagem_produto = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    observacao = db.Column(db.Text)
    preco_total = db.Column(db.Numeric(10, 2))

    def __init__(self, usuario_id, produto_id, nome_produto, quantidade, imagem_produto, observacao,preco_total):
        self.usuario_id = usuario_id
        self.produto_id = produto_id
        self.nome_produto = nome_produto
        self.quantidade = quantidade
        self.imagem_produto = imagem_produto
        self.observacao = observacao
        self.preco_total=preco_total
