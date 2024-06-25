from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import secrets
import os

# Importar a instância do banco de dados
from Model import db, Usuario
from Model.config import DATABASE

# Importe os Blueprints corretamente
# Importe os Blueprints corretamente
from controller.UsuarioController import user_bp as user_blueprint
from controller.AdminController import admin_bp as admin_blueprint
from controller.page_controller import page_bp
from controller.ProdutoController import produto_bp
from controller.CarrinhoController import cesta_bp
from controller.CestaControlle import carrinho_bp
from controller.PedidoController import pedido_bp
# Criando a instância do aplicativo Flask
app = Flask(__name__)

# Configuração da chave secreta para sessões
app.secret_key = secrets.token_hex(24)

# Configuração do SQLAlchemy com a URI do banco de dados
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração da pasta de upload de arquivos
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img', 'produtos')

# Configuração da sessão (exemplo usando filesystem)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Inicialização do SQLAlchemy
db.init_app(app)

# Registro dos Blueprints
app.register_blueprint(page_bp, name='page_bp')
app.register_blueprint(carrinho_bp, name='carrinho_bp')
app.register_blueprint(pedido_bp,name= 'pedido_bp')
app.register_blueprint(cesta_bp, url_prefix='/user', name='cesta_bp')
app.register_blueprint(user_blueprint, url_prefix='/user', name='user_bp')
app.register_blueprint(admin_blueprint, url_prefix='/admin', name='admin_bp')
app.register_blueprint(produto_bp, url_prefix='/produto', name='produto_bp')

# Inicialização do LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_bp.login'  # Aponte para a rota de login correta

# Função para carregar o usuário pelo ID
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)

if __name__ == '__main__':
    # Criação das tabelas no banco de dados
    with app.app_context():
        print("Criando tabelas no banco de dados...")
        db.create_all()
        print("Tabelas criadas com sucesso.")
    
    # Execução do aplicativo Flask
    app.run(debug=True)
