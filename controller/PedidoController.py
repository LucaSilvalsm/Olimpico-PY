from flask import Blueprint, request, redirect, url_for, flash, jsonify, session, send_from_directory
from flask_login import login_required, current_user
from Model.Pedido import Pedido
from dao.UsuarioDAO import UsuarioDAO
from dao.PedidoDAO import PedidoDAO
from dao.CarrinhoDAO import CarrinhoDAO
from Model import db
from pixqrcodegen import Payload  # Importando a classe Payload para gerar o QR Code Pix
import os
from urllib.parse import quote  # Importa a função quote
usuario_dao = UsuarioDAO()
pedido_dao = PedidoDAO()
carrinho_dao = CarrinhoDAO()

pedido_bp = Blueprint('pedido_bp', __name__)

@pedido_bp.route('/pedido', methods=['POST'])
@login_required
def criar_pedido():
    try:
        forma_pagamento = request.form['formaPagamento']
        observacao_item = []
        itens_comprados = []

        itens_carrinho = carrinho_dao.obter_itens_carrinho(current_user.id)

        for item in itens_carrinho:
            descricao_item = f"{item.nome_produto} - Observação: {item.observacao}\n"
            observacao_item.append(descricao_item)
            item_comprado = f"{item.nome_produto} - Quantidade: {item.quantidade}\n"
            itens_comprados.append(item_comprado)

        valor_total = sum(item.preco_total for item in itens_carrinho)
        usuario_data = usuario_dao.get_usuario_by_id(current_user.id)
        nome_completo = usuario_dao.nome_completo(usuario_data.nome, usuario_data.sobrenome)
        endereco_completo = usuario_dao.endereco_completo(
            usuario_data.endereco, usuario_data.numero_casa,
            usuario_data.complemento, usuario_data.bairro, usuario_data.telefone
        )

        pedido = Pedido(
            usuario_id=current_user.id,
            forma_pagamento=forma_pagamento,
            endereco_entrega=endereco_completo,
            status='Preparando',
            valor_total=valor_total,
            observacao='\n'.join(observacao_item),
            itens_comprados='\n'.join(itens_comprados)
        )

        pedido_dao.create_and_delete_carrinho(pedido, current_user.id)
        pedido_id = pedido.id

        if forma_pagamento == 'PIX':
            chave_pix = "d0cea1c5-4f6c-49a2-bd87-99906d8b52f1"
            cidade = "Duque De Caxias"
            nome_loja = "Loja"
            txtId = f"PEDIDO{pedido_id}"
            diretorio_qrcode = os.path.join(os.getcwd(), 'static', 'qrcodes')
            if not os.path.exists(diretorio_qrcode):
                os.makedirs(diretorio_qrcode)

            payload_pix = Payload(nome_loja, chave_pix, f'{valor_total:.2f}', cidade, txtId, diretorio_qrcode)
            payload_pix.gerarPayload()
            caminho_qrcode = os.path.join(diretorio_qrcode, 'pixqrcodegen.png')

            flash('Pedido criado com sucesso! Escaneie o QR Code abaixo para pagamento com PIX.', 'success')
            return redirect(url_for('page_bp.index'))

        mensagem = (
            f"Novo pedido realizado!\n\n"
            f"Código do pedido: # {pedido_id}\n"
            f"Nome: {nome_completo}\n"
            f"Endereço de Entrega \128511; : {endereco_completo}\n"
            f"Forma de Pagamento \U0001F4B3: {forma_pagamento}\n"
            f"\n\nItens Comprados \U0001F354:\n" + ''.join(itens_comprados) +
            f"\n\nObservação:\n" + ''.join(observacao_item) +
            f"\nValor Total: R$ {valor_total:.2f}"
        )
        mensagem_codificada = quote(mensagem, safe='\U0001F3E0')
        numero_telefone = "5521979844840"
        link_whatsapp = f"https://wa.me/{numero_telefone}?text={mensagem_codificada}"

        return redirect(link_whatsapp)

    except Exception as e:
        flash(f'Erro ao criar pedido: {str(e)}', 'error')
        return redirect(url_for('page_bp.index'))

@pedido_bp.route('/atualizar', methods=['POST'])
def atualizar():
    data = request.get_json()  # Receber JSON
    pedido_id = data.get('id')
    novo_status = data.get('status')

    print(f'Pedido ID: {pedido_id}, Novo Status: {novo_status}')

    # Lógica para atualizar o status no banco de dados
    pedido = Pedido.query.get(pedido_id)
    if pedido:
        pedido.status = novo_status
        db.session.commit()
        flash('Pedido Atualizado com sucesso', 'success')
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Pedido não encontrado'}), 404

def limpar_sessao_whatsapp():
    session.pop('link_whatsapp', None)
    return '', 204
