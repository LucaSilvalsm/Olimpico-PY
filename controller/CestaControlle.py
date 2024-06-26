from flask import Blueprint, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from Model.Carrinho import Carrinho
from dao.CarrinhoDAO import CarrinhoDAO
from dao.ProdutoDAO import ProdutoDAO

carrinho_dao = CarrinhoDAO()
produto_dao = ProdutoDAO()


carrinho_bp = Blueprint('carrinho_bp', __name__)

@carrinho_bp.route('/criando' , methods = ['POST'])
@login_required
def criando():
    if request.method == 'POST':
        try:
            produto_id = request.form['produto_id']
            quantidade = int(request.form['quantidade'])
            observacao = request.form['observacao']
            
            # Obtém o produto pelo ID
            produto = produto_dao.get_produto_by_id(produto_id)
            
            if not produto:
                flash('Produto não encontrado', 'error')
                return redirect(url_for('page_bp.index'))
            
            # Aqui você precisa obter a imagem do produto
            imagem_produto = produto.imagem  # Por exemplo, se 'imagem' for o nome do campo na tabela
            
            # Calcula o preço total do carrinho
            preco_total = produto.preco * quantidade
            
            # Cria o objeto Carrinho
            carrinho = Carrinho(
                usuario_id=current_user.id,
                produto_id=produto_id,
                nome_produto=produto.nome_produto,
                quantidade=quantidade,
                imagem_produto=imagem_produto,  # Certifique-se de passar imagem_produto aqui
                observacao=observacao,
                preco_total=preco_total
            )
            
            # Salva o carrinho no banco de dados usando o CarrinhoDAO
            try:
                carrinho_dao.create(carrinho)
                flash('Produto adicionado ao carrinho com sucesso!', 'success')
            except Exception as e:
                flash(f'Erro ao adicionar produto ao carrinho: {str(e)}', 'error')

            return redirect(url_for('page_bp.index'))
        
        except Exception as e:
            flash(f'Erro ao processar a requisição: {str(e)}', 'error')
            return redirect(url_for('page_bp.index'))
