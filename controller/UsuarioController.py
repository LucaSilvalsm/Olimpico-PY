from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from sqlalchemy.exc import IntegrityError
from dao.UsuarioDAO import UsuarioDAO
from Model.Usuario import Usuario
from Model.config import DATABASE

DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        numero_casa = request.form['numero_casa']
        complemento = request.form['complemento']
        bairro = request.form['bairro']
        senha = request.form['senha']
        confirmacaoSenha = request.form['confirmacaoSenha']

        # Verificar se as senhas correspondem
        if senha != confirmacaoSenha:
            flash('As senhas não correspondem', 'error')
            return redirect(url_for('user_bp.register'))

        # Criar uma nova instância do usuário
        novo_usuario = Usuario(
            nome=nome,
            sobrenome=sobrenome,
            telefone=telefone,
            email=email,
            senha=senha,  # Armazenar a senha como uma string sem hash (não recomendado em produção)
            endereco=endereco,
            numero_casa=numero_casa,
            bairro=bairro,
            complemento=complemento
        )

        # Usando o DAO para incluir o usuário no banco de dados
        dao = UsuarioDAO()
        try:
            # Verificar se email já está cadastrado
            if dao.obter_por_email(email):
                flash('Email já cadastrado', 'error')
                return redirect(url_for('user_bp.register'))

            dao.incluir(novo_usuario)
            flash('Usuário registrado com sucesso!', 'success')
            return redirect(url_for('user_bp.login'))  # Redirecionar para o endpoint 'login' do Blueprint 'user_bp'

        except IntegrityError as e:
            flash(f'Erro ao registrar usuário: {str(e)}', 'error')
            return redirect(url_for('user_bp.register'))

        except Exception as e:
            flash(f'Erro ao registrar usuário: {str(e)}', 'error')
            return redirect(url_for('user_bp.register'))

        finally:
            dao.close()

    # Se o método HTTP não for POST (pode ser GET), renderizar o formulário de registro
    return render_template('cadastro.html')

@user_bp.route('/login', methods=['POST', 'GET'])
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
                return redirect(url_for('user_bp.login'))

        except Exception as e:
            flash(f'Erro ao realizar login: {str(e)}', 'error')
            return redirect(url_for('user_bp.login'))

        finally:
            dao.close()

    # Se o método HTTP for GET, renderize o formulário de login
    return render_template('login.html')


@user_bp.route('/logout')
def logout():
    # Limpar sessão
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('page_bp.index'))