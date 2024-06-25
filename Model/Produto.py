from Model import db

class Produto(db.Model):
    __tablename__ = 'produto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produto = db.Column(db.String(200), nullable=False)
    tipo_produto = db.Column(db.String(200))
    tamanho = db.Column(db.String(200))
    ingrediente = db.Column(db.String(200))
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    descricao = db.Column(db.Text)
    imagem = db.Column(db.String(250))
    

    def __init__(self, nome_produto, tipo_produto, tamanho, ingrediente, preco, descricao=None, imagem=None):
        self.nome_produto = nome_produto
        self.tipo_produto = tipo_produto
        self.tamanho = tamanho
        self.ingrediente = ingrediente
        self.preco = preco
        self.descricao = descricao
        self.imagem = imagem