from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
import os

from Model import db, Usuario

from controller.UsuarioController import user_bp as user_blueprint
from controller.AdminController import admin_bp as admin_blueprint
from controller.page_controller import page_bp
from controller.ProdutoController import produto_bp
from controller.CarrinhoController import cesta_bp
from controller.CestaControlle import carrinho_bp
from controller.PedidoController import pedido_bp

app = Flask(__name__)


# ✅ Chave secreta fixa via variável de ambiente
app.secret_key = os.environ.get('SECRET_KEY', 'chave-local-dev')

# ✅ Banco lido da variável que a Railway injeta automaticamente
database_url = os.environ.get('DATABASE_URL', '')

# ✅ Railway entrega "postgres://" mas SQLAlchemy exige "postgresql://"
if database_url.startswith('postgres://'):
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Sessão via banco de dados (funciona em ambiente serverless/Railway)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img', 'produtos')

db.init_app(app)

# Sessão precisa ser iniciada após db.init_app
Session(app)
csrf = CSRFProtect(app)

app.register_blueprint(page_bp, name='page_bp')
app.register_blueprint(carrinho_bp, name='carrinho_bp')
app.register_blueprint(pedido_bp, name='pedido_bp')
app.register_blueprint(cesta_bp, url_prefix='/user', name='cesta_bp')
app.register_blueprint(user_blueprint, url_prefix='/user', name='user_bp')
app.register_blueprint(admin_blueprint, url_prefix='/admin', name='admin_bp')
app.register_blueprint(produto_bp, url_prefix='/produto', name='produto_bp')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_bp.login'

@login_manager.unauthorized_handler
def unauthorized():
    flash('Necessário estar logado para acessar esta página.', 'error')
    return redirect(url_for('page_bp.login'))

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, user_id)

if __name__ == '__main__':
    with app.app_context():
        print("Criando tabelas no banco de dados...")
        db.create_all()
        print("Tabelas criadas com sucesso.")
    app.run(debug=True)

