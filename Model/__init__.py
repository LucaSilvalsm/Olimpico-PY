from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from  Model.Usuario import Usuario, UsuarioAdmin
from Model.Produto import Produto
from Model.Carrinho import Carrinho
from Model.Pedido import Pedido