from flask import Flask, Blueprint, request, redirect, url_for, flash, render_template, current_app
from werkzeug.utils import secure_filename
import os
from Model.Produto import Produto
from dao.ProdutoDAO import ProdutoDAO
from Model.Pedido import Pedido
from dao.PedidoDAO import PedidoDAO

# Configuração do Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Defina sua chave secreta para o uso de flash messages

# Configurações específicas para uploads de arquivos
UPLOAD_FOLDER = 'static/img/produtos'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Registro do Blueprint para produtos
produto_bp = Blueprint('produto_bp', __name__)
produtoDao = ProdutoDAO()

# Função para verificar extensões permitidas
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota para registrar um novo produto
@produto_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        try:
            # Obter os dados do formulário
            nome_produto = request.form['nome']
            tipo_produto = request.form['tipoProdutos']

            # Processar tamanhos selecionados
            tamanhos_selecionados = request.form.getlist('tamanho[]')
            tamanho = ','.join(tamanhos_selecionados)

            # Processar ingredientes selecionados
            ingredientes_selecionados = request.form.getlist('ingrediente[]')
            ingrediente = ' - '.join(ingredientes_selecionados)

            preco = request.form['preco']
            descricao = request.form['descricao']
            imagem = request.files['image'] if 'image' in request.files else None

            # Processar o arquivo de imagem e definir o nome da imagem
            if imagem and allowed_file(imagem.filename):
                nome_imagem = secure_filename(imagem.filename)
                path_imagem = os.path.join(current_app.config['UPLOAD_FOLDER'], nome_imagem)
                print(f'Saving image to: {path_imagem}')  # Debug: verificar o caminho da imagem
                imagem.save(path_imagem)
            else:
                flash('Erro ao processar imagem', 'error')
                return redirect(url_for('page_bp.produto'))

            # Criar um novo objeto Produto com todos os dados
            novo_produto = Produto(
                nome_produto=nome_produto,
                tipo_produto=tipo_produto,
                tamanho=tamanho,
                ingrediente=ingrediente,
                preco=float(preco),
                descricao=descricao,
                imagem=nome_imagem
            )

            # Incluir o novo produto no banco de dados
            produtoDao.incluir(novo_produto)
            flash('Produto adicionado com sucesso!', 'success')

            return redirect(url_for('page_bp.produto'))

        except Exception as e:
            flash(f'Erro ao adicionar produto: {str(e)}', 'error')
            return redirect(url_for('page_bp.produto'))

    # Redirecionar para a página de produtos em caso de erro
    return redirect(url_for('page_bp.produto'))

# Rota para deletar um produto
@produto_bp.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        produto_id = request.form['id']

        # Verificar se o produto existe antes de excluir
        produto = produtoDao.obter(produto_id)
        if produto:
            try:
                produtoDao.excluir(produto_id)
                flash(f'Produto ID  excluído com sucesso!', 'success')
            except Exception as e:
                flash(f'Erro ao excluir produto: {str(e)}', 'error')
        else:
            flash(f'Produto não encontrado para exclusão', 'error')

        return redirect(url_for('page_bp.all_produtos'))

    # Redirecionar para a página de produtos em caso de erro
    return redirect(url_for('page_bp.all_produtos'))

# Registrar o blueprint para produtos
app.register_blueprint(produto_bp)

if __name__ == "__main__":
    app.run(debug=True)


