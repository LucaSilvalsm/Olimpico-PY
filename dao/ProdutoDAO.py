from Model import db
from Model.Produto import Produto
import secrets

class ProdutoDAO:
    def __init__(self):
        pass
    
    def incluir(self, produto):
        try:
            db.session.add(produto)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    
    def get_produto_by_id(self, produto_id):
        return Produto.query.get(produto_id)
    
    def image_generate_name(self):
        return secrets.token_hex(30) + ".jpg"
    
    def alterar(self, produto_id, novo_produto):
        try:
            prod = self.get_produto_by_id(produto_id)
            prod.nome_produto = novo_produto.nome_produto
            prod.tipo_produto = novo_produto.tipo_produto
            prod.tamanho = novo_produto.tamanho
            prod.ingrediente = novo_produto.ingrediente
            prod.preco = novo_produto.preco
            prod.descricao = novo_produto.descricao
            prod.imagem = novo_produto.imagem
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    
    def excluir(self, id):
        produto = Produto.query.get(id)
        if produto:
            db.session.delete(produto)
            db.session.commit()
    def obter_todos(self):
        return Produto.query.all()
    
    def tipo_produto(self, tipo_produto):
        
        return Produto.query.filter_by(tipo_produto=tipo_produto).all()
    
    def obter(self, chave):
        return Produto.query.get(chave)
    
    def image_generate_name(self):
        return secrets.token_hex(60) + ".jpg"
    
    def todas_categorias(self):
        categorias = ["Artesanal", "Tradicional", "Bebida", "Porcao", "Sobremesa"]
        produtos_por_categoria = {}

        for categoria in categorias:
            produtos_categoria = self.tipo_produto(categoria)
            produtos_por_categoria[categoria] = produtos_categoria

        return produtos_por_categoria
    
    def close(self):
        db.session.close()