from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user,logout_user
from Model import db, Usuario
from dao.UsuarioDAO import UsuarioDAO

user_bp = Blueprint('user_bp', __name__)

# Instância do DAO para manipulação de usuários
usuario_dao = UsuarioDAO()

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        endereco = request.form['endereco']
        numero_casa = request.form['numero_casa']
        complemento = request.form['complemento']  # Corrigido o nome do campo
        bairro = request.form['bairro']
        telefone = request.form['telefone']
        email = request.form['email']
        senha = request.form['senha']
        confirmacaoSenha = request.form['confirmacaoSenha']

        # Verifica se o email já está cadastrado
        if usuario_dao.obter_por_email(email):
            flash('Este email já está sendo utilizado.', 'error')
            return redirect(url_for('user_bp.register'))

        # Verifica se as senhas coincidem
        if senha != confirmacaoSenha:
            flash('As senhas não coincidem.', 'error')
            return redirect(url_for('user_bp.register'))

        # Cria um novo usuário
        novo_usuario = Usuario(nome=nome, sobrenome=sobrenome, endereco=endereco,
                               numero_casa=numero_casa, complemento=complemento,
                               bairro=bairro, telefone=telefone, email=email, senha=senha)

        # Adiciona o usuário ao banco de dados
        try:
            usuario_dao.incluir(novo_usuario)
            flash('Cadastro realizado com sucesso!', 'success')

            # Autentica o usuário após o registro
            login_user(novo_usuario)

            return redirect(url_for('user_bp.login'))  # Redireciona para o perfil do usuário após o registro
        except Exception as e:
            flash('Erro ao cadastrar usuário. Tente novamente.', 'error')
            return redirect(url_for('user_bp.register'))

    return render_template('login.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        # Verificar se o email e senha estão presentes
        if email and senha:
            # Buscar o usuário pelo email
            usuario = Usuario.query.filter_by(email=email).first()

            # Verificar se o usuário existe e a senha está correta
            if usuario and usuario.senha == senha:
                # Autenticar o usuário usando Flask-Login
                login_user(usuario)

                # Redirecionar para a página após o login
                # Aqui você pode redirecionar para a página inicial do usuário, por exemplo
                return redirect(url_for('page_bp.index'))

            # Se o email ou senha estiverem incorretos
            flash('Credenciais inválidas. Verifique seu email e senha.', 'error')

        else:
            flash('Por favor, forneça seu email e senha.', 'error')

    # Se for método GET ou se houver um erro de login, renderizar o formulário de login
    return render_template('login.html')

@user_bp.route('/logout')
def logout():
    # Utiliza o método do Flask-Login para deslogar o usuário
    logout_user()

    # Flash message opcional para informar o usuário que ele foi deslogado com sucesso
    flash('Você foi deslogado com sucesso.', 'success')

    # Redireciona para a página de login, ou para onde desejar após o logout
    return redirect(url_for('user_bp.login'))
    