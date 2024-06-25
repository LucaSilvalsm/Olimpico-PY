from Model import db
from Model.Pedido import Pedido
from Model.Carrinho import Carrinho

class PedidoDAO:

    def create(self, pedido):
        try:
            db.session.add(pedido)
            db.session.commit()
            return pedido
        except Exception as e:
            db.session.rollback()
            raise e

    def create_and_delete_carrinho(self, pedido, usuario_id):
        try:
            db.session.add(pedido)
            db.session.commit()

            # Obtenha o ID do pedido recém-inserido
            id_pedido = pedido.id

            # Exclua os itens do carrinho associados ao usuário
            db.session.query(Carrinho).filter_by(usuario_id=usuario_id).delete()
            db.session.commit()

            return id_pedido
        except Exception as e:
            db.session.rollback()
            raise e

    def obter_pedidos_por_usuario_id(self, usuario_id):
        try:
            pedidos = Pedido.query.filter_by(usuario_id=usuario_id).order_by(Pedido.data_pedido.desc()).all()
            return pedidos
        except Exception as e:
            raise e

    def obter_pedido_por_id(self, pedido_id):
        try:
            pedido = Pedido.query.get(pedido_id)
            return pedido
        except Exception as e:
            raise e
