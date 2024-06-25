# controller/page_controller.py
from flask import Blueprint, render_template, flash, redirect, url_for, session,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.config import DATABASE
from dao.ProdutoDAO import ProdutoDAO
from dao.CarrinhoDAO import CarrinhoDAO
from dao.UsuarioDAO import UsuarioDAO
from Model.Usuario import Usuario
from flask_login import current_user,login_required
from Model.Pedido import Pedido
from dao.PedidoDAO import PedidoDAO


page_bp = Blueprint('page_bp', __name__)
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

page_bp = Blueprint('page_bp', __name__)
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

@page_bp.route('/')
def index():
    produto_dao = ProdutoDAO()  # Criar uma instância válida de ProdutoDAO
    artesanais = produto_dao.tipo_produto("Artesanal")  # Chamar o método tipo_produto com o tipo desejado
    tradicionais = produto_dao.tipo_produto("Tradicional")
    bebidas = produto_dao.tipo_produto("Bebida")
    porcao = produto_dao.tipo_produto("Porcao")
    print("Acessando a rota /")
    print(artesanais)  # Apenas para debug, para verificar se os produtos foram obtidos corretamente
    return render_template("index.html", artesanais=artesanais,tradicionais=tradicionais,bebidas=bebidas, porcao=porcao)


@page_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        dao = UsuarioDAO()
        try:
            usuario = dao.obter_por_email(email)

            if usuario and usuario.senha == senha:  # Verifica a senha (sem hash)
                session['usuario_id'] = usuario.id
                session['usuario_nome'] = usuario.nome
                session['tipo_usuario'] = usuario.tipo_usuario  # Agora o tipo de usuário é recuperado do banco de dados
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('page_bp.index'))  # Redireciona para a página inicial após o login

            else:
                flash('Credenciais inválidas. Verifique seu email e senha.', 'error')
                return redirect(url_for('page_bp.login'))

        except Exception as e:
            flash(f'Erro ao realizar login: {str(e)}', 'error')
            return redirect(url_for('page_bp.login'))

        finally:
            dao.close()

    # Se o método HTTP for GET, renderize o formulário de login
    return render_template('login.html')
@page_bp.route("/admin_login")
def admin_login():
    print("Acessando a rota /admin_login")
    return render_template('login_adm.html')



@page_bp.route("/cadastro")
def cadastro():
    print("Acessando a rota /cadastro")
    return render_template('cadastro.html')


@page_bp.route('/pedidos' , methods = ['GET'])
@login_required
def pedidos():
    try:
        pedido_dao = PedidoDAO()
        # Obter todos os pedidos do usuário atual
        pedidos = pedido_dao.obter_pedidos_por_usuario_id(current_user.id)
        
        # Renderizar o template 'pedidos.html' passando a lista de pedidos
        return render_template('pedidos.html', pedidos=pedidos)
    
    except Exception as e:
        # Em caso de erro, trate de acordo com sua lógica de manipulação de erros
        return render_template('error.html', error=str(e))
@page_bp.route('/cesta', methods=['GET'])
def cesta():
    if current_user.is_authenticated:
        usuario_id = current_user.id  # Obtém o ID do usuário autenticado
        usuario_dao = UsuarioDAO()
        carrinho_dao = CarrinhoDAO()
        
        try:
            itens_carrinho = carrinho_dao.obter_itens_carrinho(usuario_id)  # Obtém os itens de carrinho do usuário
            usuario_data = usuario_dao.get_usuario_by_id(usuario_id)  # Obtém os dados do usuário
            
            # Calcular o total do carrinho
            total_carrinho = sum(carrinho.preco_total for carrinho in itens_carrinho)
            total_carrinho_formatado = '{:.2f}'.format(total_carrinho)
            
            carrinho_dao.close()
            usuario_dao.close()
            
            return render_template('cesta.html', itens_carrinho=itens_carrinho, usuario_data=usuario_data, total_carrinho=total_carrinho_formatado)
        
        except Exception as e:
            flash(f'Erro ao carregar cesta: {str(e)}', 'error')
            return redirect(url_for('page_bp.index'))  # Redireciona para a página inicial em caso de erro
    
    flash('Faça o Login para Continuar', 'warning')
    return redirect(url_for('user_bp.login'))
    
@page_bp.route("/cadastro_admin")
def cadastro_admin():
    print("Acessando a rota /cadastro_admin")
    return render_template('cadastro_admin.html')

@page_bp.route("/painel")
def painel():
    print("Acessando a rota /painel")
    return render_template('./admin/painel.html')

@page_bp.route('/dashboard')
def dashboard():
    return render_template('/admin/painel.html')

@page_bp.route("/produto")
def produto():
    print("Acessando a rota /produto")
    return render_template('./admin/newproduto.html')

@page_bp.route("/all_produtos")
def all_produtos():
    try:
        produto_dao = ProdutoDAO()  # Instanciação correta do ProdutoDAO
        produtos = produto_dao.todas_categorias()
        print("Acessando a rota /all_produtos")
        return render_template('./admin/all_produtos.html', produtos=produtos)
    except Exception as e:
        flash(f'Erro ao carregar produtos: {str(e)}', 'error')
        return redirect(url_for('page_bp.index'))
    finally:
        produto_dao.close()  # Certifica-se de fechar a sessão do banco de dados

@page_bp.route("/criando_teste")
def criando_teste():
    
    print('caiu aqui')




##Testando o detalhe pedido  ## As rotas dos pedidos

@page_bp.route("/produto/<int:produto_id>", methods=['GET'])
def detalhes_produto(produto_id):
    produto_dao = ProdutoDAO()
    produto = produto_dao.get_produto_by_id(produto_id)
    if not produto:
        return render_template('produto_nao_encontrado.html')
    print(f"Acessando detalhes do produto rota produto: {produto}")
    return render_template('detalhes_produto.html', produto=produto)
#detalhe porcao
@page_bp.route('/porcao/<int:produto_id>', methods=['GET'])
def detalhes_porcao(produto_id):
    # Verificar se o usuário está logado
    if 'usuario_id' not in session:
        # Se não estiver logado, redirecione para a página de login
        return redirect(url_for('page_bp.login'))

    # Se o usuário estiver logado, continuar com a obtenção do produto
    produto_dao = ProdutoDAO()
    produto = produto_dao.get_produto_by_id(produto_id)
    
    if not produto:
        print(f"Produto ID {produto_id} não encontrado")
        return render_template('produto_nao_encontrado.html')
 
    print(f"Detalhes do produto encontrado: {produto}")
    return render_template('detalhes_porcao.html', produto=produto)


@page_bp.route('/bebidas/<int:produto_id>', methods=['GET'])
def detalhes_bebida(produto_id):
    produto_dao = ProdutoDAO()
    produto = produto_dao.get_produto_by_id(produto_id)
    if not produto:
        print(f"Produto ID {produto_id} não encontrado")
        return render_template('produto_nao_encontrado.html')
 
    print(f"Detalhes do produto encontrado: {produto}")
    return render_template('detalhes_bebida.html', produto=produto)

