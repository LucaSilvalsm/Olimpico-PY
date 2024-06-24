from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from dao.CarrinhoDAO import CarrinhoDAO
from Model.Carrinho import Carrinho

from dao.ProdutoDAO import ProdutoDAO
from dao.UsuarioDAO import UsuarioDAO
from Model.config import DATABASE


cesta_bp = Blueprint('cesta_bp', __name__)

produto_dao = ProdutoDAO()
usuario_dao = UsuarioDAO()
carrinho_dao = CarrinhoDAO()

@cesta_bp.route('/add', methods=['POST'])
def add_to_cart():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para adicionar ao carrinho', 'error')
        return redirect(url_for('user_bp.login'))
    
    usuario_id = session['usuario_id']
    produto_id = request.form['produto_id']
    quantidade = int(request.form['quantidade'])
    observacao = request.form['observacao']
    
    produto = produto_dao.get_produto_by_id(produto_id)
    if not produto:
        flash('Produto não encontrado', 'error')
        return redirect(url_for('page_bp.index'))
    
    preco_total = produto.preco * quantidade
    
    carrinho = Carrinho(
        usuario_id=usuario_id,
        produto_id=produto_id,
        nome_produto=produto.nome_produto,
        imagem_produto=produto.imagem,
        quantidade=quantidade,
        observacao=observacao,
        preco_total=preco_total
    )
    
    try:
        carrinho_dao.create(carrinho)
        flash('Produto adicionado ao carrinho com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao adicionar produto ao carrinho: {str(e)}', 'error')

    return redirect(url_for('page_bp.index'))
