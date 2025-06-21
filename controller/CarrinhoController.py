from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from Model.Carrinho import Carrinho
from dao.CarrinhoDAO import CarrinhoDAO
from dao.ProdutoDAO import ProdutoDAO  # Certifique-se de importar corretamente o ProdutoDAO

cesta_bp = Blueprint('cesta_bp', __name__)

carrinho_dao = CarrinhoDAO()
produto_dao = ProdutoDAO()

@cesta_bp.route('/criando', methods=['POST'])
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
            
            # Calcula o preço total do carrinho
            preco_total = produto.preco * quantidade
            
            # Cria o objeto Carrinho
            carrinho = Carrinho(
                usuario_id=current_user.id,  # Assume-se que o ID do usuário está disponível via Flask-Login
                produto_id=produto_id,
                nome_produto=produto.nome_produto,
                
                quantidade=quantidade,
                observacao=observacao,
                preco_total=preco_total
            )
            
            # Logo após obter os dados do formulário
            print(f"produto_id: {produto_id}, quantidade: {quantidade}, observacao: {observacao}")

            # Antes de criar o objeto Carrinho
            print(f"ID do usuário: {current_user.id}, nome do produto: {produto.nome_produto}, preco_total: {preco_total}")

            # Antes de salvar no banco de dados
           
            print(f"Carrinho a ser salvo: {carrinho}")
            # Salva o carrinho no banco de dados usando o CarrinhoDAO
            try:
                carrinho_dao.create(carrinho)
                flash('Produto adicionado ao carrinho com sucesso!', 'success')
                print(f"Carrinho a ser salvo: {carrinho}")
            except Exception as e:
                flash(f'Erro ao adicionar produto ao carrinho: {str(e)}', 'error')

            return redirect(url_for('page_bp.index'))
        
        except Exception as e:
            flash(f'Erro ao processar a requisição: {str(e)}', 'error')
            return redirect(url_for('page_bp.index'))

@cesta_bp.route('/delete', methods=['POST'])
@login_required
def delete():
    try:
        carrinho_id = request.form['id']

        carrinho = carrinho_dao.obter(carrinho_id)
        if carrinho:
            carrinho_dao.delete(carrinho.id)
            flash(f'Produto removido do carrinho com sucesso', 'success')
        else:
            flash(f'Carrinho ID {carrinho_id} não encontrado para excluir', 'error')
    except Exception as e:
        flash(f'Erro ao excluir o carrinho: {str(e)}', 'error')

    return redirect(url_for('page_bp.cesta'))  # Certifique-se de ajustar o redirecionamento conforme necessário
