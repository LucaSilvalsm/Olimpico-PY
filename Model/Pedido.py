from Model import db

class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data_pedido = db.Column(db.DateTime, default=db.func.current_timestamp())
    forma_pagamento = db.Column(db.String(100))
    endereco_entrega = db.Column(db.String(400))
    status = db.Column(db.String(100))
    valor_total = db.Column(db.Numeric(10, 2))
    observacao = db.Column(db.Text)
    itens_comprados = db.Column(db.Text)
    
