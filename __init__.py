from flask_sqlalchemy import SQLAlchemy



from Model.Usuario import Usuario
from Model.Usuario import UsuarioAdmin
from Model.Produto import Produto
from Model.Carrinho import Carrinho
from Model.Pedido import Pedido
from pixqrcodegen import *


db = SQLAlchemy()