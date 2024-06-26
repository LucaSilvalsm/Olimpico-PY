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

            # Excluir os itens do carrinho associados ao usuário
            db.session.query(Carrinho).filter_by(usuario_id=usuario_id).delete()
            db.session.commit()

            return id_pedido
        except Exception as e:
            db.session.rollback()
            raise e

    def obter_todos_os_pedidos(self):
        try:
            pedidos = Pedido.query.order_by(Pedido.data_pedido.desc()).all()
            return pedidos
        except Exception as e:
            raise e

    def obter_ultimos_10_pedidos(self):
        try:
            pedidos = Pedido.query.order_by(Pedido.data_pedido.desc()).limit(10).all()
            return pedidos
        except Exception as e:
            raise e

   

    def obter_pedidos_por_usuario_id(self, usuario_id):
        try:
            pedidos = Pedido.query.filter_by(usuario_id=usuario_id).order_by(Pedido.data_pedido.desc()).all()
            return pedidos
        except Exception as e:
            raise e
    

   
    def deletar(self, pedido_id):
        try:
            pedido = Pedido.query.filter_by(id=pedido_id).first()
            if pedido:
                db.session.delete(pedido)
                db.session.commit()
                return True
            return False  # Retorna False se o pedido não existir
        except Exception as e:
            db.session.rollback()
            raise e
    def atualizar_status_pedido(self, pedido_id, novo_status):
        try:
            pedido = Pedido.query.filter_by(id=pedido_id).first()
            if pedido:
                pedido.status = novo_status
                db.session.commit()
                return True
            return False  # Retorna False se o pedido não existir
        except Exception as e:
            db.session.rollback()
            raise e
    def calcular_valor_total_dos_pedidos(self):
        try:
            pedidos = Pedido.query.all()
            total = sum(pedido.valor_total for pedido in pedidos)
            return total
        except Exception as e:
            raise e
    def contar_quantidade_de_pedidos(self):
        try:
            quantidade = Pedido.query.count()
            return quantidade
        except Exception as e:
            raise e
    def calcular_media_dos_pedidos(self):
        try:
            pedidos = Pedido.query.all()
            if not pedidos:
                return "0.00"  # Retorna "0.00" se não houver pedidos na base de dados
            
            total = sum(pedido.valor_total for pedido in pedidos)
            quantidade = len(pedidos)
            if quantidade == 0:
                return "0.00"  # Retorna "0.00" se não houver pedidos (proteção contra divisão por zero)
            
            media = total / quantidade
            media_formatada = "{:.2f}".format(media)  # Formata a média para duas casas decimais
            return media_formatada
        except Exception as e:
            raise e
    def obter_id(self, pedido_id):
        return db.session.get(Pedido, pedido_id)
