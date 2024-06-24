from Model import db
from Model.Carrinho import Carrinho


class CarrinhoDAO:
    def __init__(self):
        pass
    
    def incluir(self, carrinho):
        try:
            db.session.add(carrinho)
            db.session.commit()
            return carrinho
        except Exception as e:
            db.session.rollback()
            raise e
    
    def get_carrinho_by_id(self, carrinho_id):
        return Carrinho.query.get(carrinho_id)
    
    def excluir(self, id):
        carrinho = Carrinho.query.get(id)
        if carrinho:
            db.session.delete(carrinho)
            db.session.commit()
    
    def obter_todos(self):
        return Carrinho.query.all()
    
    def obter_por_usuario(self, usuario_id):
        return Carrinho.query.filter_by(usuario_id=usuario_id).all()
    
    def close(self):
        db.session.close()
