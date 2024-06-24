from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Model import db
from Model import Usuario,Carrinho,Pedido,Produto
from controller.UsuarioController import user_bp as user_blueprint
from controller.AdminController import admin_bp as admin_blueprint
from controller.page_controller import page_bp
from controller.ProdutoController import produto_bp
from controller.CarrinhoController import cesta_bp
from Model.config import DATABASE
import secrets
import os

app = Flask(__name__)

# Definindo a chave secreta para sessões
app.secret_key = secrets.token_hex(24)

# Configuração do SQLAlchemy com a URI do banco de dados
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'img', 'produtos')

# Inicialização do SQLAlchemy com o aplicativo Flask
db.init_app(app)

# Registro dos Blueprints
app.register_blueprint(page_bp)
app.register_blueprint(cesta_bp, url_prefix='/user', name='cesta_bp')
app.register_blueprint(user_blueprint, url_prefix='/user', name='user_bp')
app.register_blueprint(admin_blueprint, url_prefix='/admin', name='admin_bp')
app.register_blueprint(produto_bp, url_prefix='/produto')

pedidos = db.relationship(Pedido, backref='usuario', lazy=True)
carrinho = db.relationship(Carrinho, backref='usuario', lazy=True)
usuario = db.relationship(Usuario, backref='pedidos', lazy=True)
carrinhos = db.relationship(Carrinho, backref='produto', lazy=True)
usuario = db.relationship(Usuario, backref='carrinho', lazy=True)
produto = db.relationship(Produto, backref='carrinhos', lazy=True)






if __name__ == '__main__':
    app.run(debug=True)
