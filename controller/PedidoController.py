from flask import Blueprint, request, redirect, url_for, flash
from flask_login import login_required, current_user
from Model.Pedido import Pedido
from dao.UsuarioDAO import UsuarioDAO
from dao.PedidoDAO import PedidoDAO
from dao.CarrinhoDAO import CarrinhoDAO

usuario_dao = UsuarioDAO()
pedido_dao = PedidoDAO()
carrinho_dao = CarrinhoDAO()

pedido_bp = Blueprint('pedido_bp', __name__)

@pedido_bp.route('/pedido', methods=['POST'])
@login_required
def criar_pedido():
    try:
        forma_pagamento = request.form['formaPagamento']

        # Inicializar listas para armazenar observações e itens comprados
        observacao_item = []
        itens_comprados = []

        # Obter itens do carrinho do usuário
        itens_carrinho = carrinho_dao.obter_itens_carrinho(current_user.id)

        # Montar a lista de itens comprados no formato desejado
        for item in itens_carrinho:
            # Formatar cada item do carrinho para observacao_item
            descricao_item = f"{item.nome_produto}  - Observação: {item.observacao}"
            observacao_item.append(descricao_item)

            # Formatar cada item do carrinho para itens_comprados
            item_comprado = f"{item.nome_produto} - Quantidade: {item.quantidade}"
            itens_comprados.append(item_comprado)

        # Calcular o valor total do pedido
        valor_total = sum(item.preco_total for item in itens_carrinho)

        # Obter dados do usuário para o endereço completo
        usuario_data = usuario_dao.get_usuario_by_id(current_user.id)
        endereco_completo = usuario_dao.endereco_completo(
            usuario_data.endereco, usuario_data.numero_casa,
            usuario_data.complemento, usuario_data.bairro, usuario_data.telefone
        )

        # Criar o objeto Pedido
        pedido = Pedido(
            usuario_id=current_user.id,
            forma_pagamento=forma_pagamento,
            endereco_entrega=endereco_completo,
            status='PENDENTE',  # Defina o status inicial do pedido
            valor_total=valor_total,
            observacao='\n'.join(observacao_item),  # Concatenar todas as observações dos itens
            itens_comprados='\n'.join(itens_comprados)  # Concatenar todos os itens comprados
        )

        # Salvar o pedido no banco de dados e limpar o carrinho do usuário
        pedido_dao.create_and_delete_carrinho(pedido, current_user.id)

        flash('Pedido realizado com sucesso!', 'success')
        return redirect(url_for('page_bp.index'))  # Redirecionar para a página inicial após o pedido ser criado

    except Exception as e:
        flash(f'Erro ao criar pedido: {str(e)}', 'error')
        return redirect(url_for('page_bp.index'))
