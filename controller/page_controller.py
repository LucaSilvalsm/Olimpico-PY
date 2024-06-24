# controller/page_controller.py
from flask import Blueprint, render_template,flash,redirect,url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.config import DATABASE
from dao.ProdutoDAO import ProdutoDAO

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
    return render_template("index.html", artesanais=artesanais,tradicionais=tradicionais,bebidas=bebidas, porcao=porcao)  # Passar os produtos obtidos para o template
@page_bp.route("/login")
def login():
    print("Acessando a rota /login")
    return render_template('login.html')

@page_bp.route("/admin_login")
def admin_login():
    print("Acessando a rota /admin_login")
    return render_template('login_adm.html')



@page_bp.route("/cadastro")
def cadastro():
    print("Acessando a rota /cadastro")
    return render_template('cadastro.html')


@page_bp.route("/cesta")
def cesta():
    print("Acessando a rota /cesta")
    return render_template('cesta.html')

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






##Testando o detalhe pedido  ## As rotas dos pedidos

@page_bp.route('/produto/<int:produto_id>', methods=['GET'])
def detalhes_produto(produto_id):
    produto_dao = ProdutoDAO()
    produto = produto_dao.get_produto_by_id(produto_id)
    if not produto:
        print(f"Produto ID {produto_id} não encontrado")
        return render_template('produto_nao_encontrado.html')
 
    print(f"Detalhes do produto encontrado: {produto}")
    return render_template('detalhes_produto.html', produto=produto)


#detalhe porcao
@page_bp.route('/porcao/<int:produto_id>', methods=['GET'])
def detalhes_porcao(produto_id):
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

