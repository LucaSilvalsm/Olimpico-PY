from Model import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200))
    numero_casa = db.Column(db.String(20))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    tipo_usuario = db.Column(db.String(20), default='Cliente')

    carrinhos = db.relationship('Carrinho', backref='usuario', lazy=True)
    pedidos = db.relationship('Pedido', backref='usuario', lazy=True)

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
        self.tipo_usuario = 'Cliente'


    def get_id(self):
        return str(self.id)

    @property
    def is_active(self):
        # Aqui, você pode adicionar lógica para verificar se o usuário está ativo.
        # Por exemplo, se você tiver um campo `ativo` no banco de dados:
        # return self.ativo
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
class UsuarioAdmin(db.Model):
    __tablename__ = 'usuarioadmin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200))
    sobrenome = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200))
    tipo_cliente = db.Column(db.String(50), default='Administrador')

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
    def get_id(self):
        return str(self.id)
    def serialize(self):
        return {
            "ID": self.id,
            "Nome": self.nome,
            "Sobrenome": self.sobrenome,
            "Email": self.email,
            "Tipo de Cliente": self.tipo_cliente
            # Adicione mais campos conforme necessário
        }

    @property
    def is_active(self):
        # Aqui, você pode adicionar lógica para verificar se o usuário está ativo.
        # Por exemplo, se você tiver um campo `ativo` no banco de dados:
        # return self.ativo
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
