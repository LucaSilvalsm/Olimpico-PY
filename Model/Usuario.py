from Model import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))
    numero_casa = db.Column(db.String(20))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    tipo_usuario = db.Column(db.String(20), default='Cliente')  # Definindo o tipo_usuario como 'Cliente' por padrão

    def __init__(self, nome, sobrenome, telefone, email, senha, endereco=None, numero_casa=None, complemento=None, bairro=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.numero_casa = numero_casa
        self.complemento = complemento
        self.bairro = bairro
        # Definindo tipo_usuario como 'Cliente' por padrão
        self.tipo_usuario = 'Cliente'
        
class UsuarioAdmin(db.Model):
    __tablename__ = 'usuarioadmin'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    sobrenome = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200))
    tipo_cliente = db.Column(db.String(50), default='Administrador')  # Definindo o tipo_cliente como 'Administrador' por padrão

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha