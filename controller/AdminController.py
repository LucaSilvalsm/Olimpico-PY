#AdminController
from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from sqlalchemy.exc import IntegrityError
from dao.UsuarioAdminDAO import UsuarioAdminDAO
from Model.Usuario import UsuarioAdmin
from Model.config import DATABASE

DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"


admin_bp = Blueprint('user_bp', __name__)

@admin_bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Pegando os dados do formulário
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        confirmacaoSenha = request.form['confirmacaoSenha']

        # Verificar se as senhas correspondem
        if senha != confirmacaoSenha:
            flash('As senhas não correspondem', 'error')
            return redirect(url_for('admin_bp.register'))

        # Criar uma nova instância do usuário administrativo
        novo_usuario_admin = UsuarioAdmin(
            nome=nome,
            sobrenome=sobrenome,
            email=email,
            senha=senha  # Armazenar a senha como uma string sem hash (não recomendado em produção)
        )

        # Usando o DAO para incluir o usuário no banco de dados
        dao = UsuarioAdminDAO()
        try:
            # Verificar se email já está cadastrado
            if dao.obter_por_email(email):
                flash('Email já cadastrado', 'error')
                return redirect(url_for('admin_bp.register'))

            dao.incluir(novo_usuario_admin)
            flash('Usuário administrativo registrado com sucesso!', 'success')
            return redirect(url_for('admin_bp.login'))  # Redirecionar para o endpoint 'login' do Blueprint 'user_bp'

        except IntegrityError as e:
            flash(f'Erro ao registrar usuário administrativo: {str(e)}', 'error')
            return redirect(url_for('admin_bp.register'))

        except Exception as e:
            flash(f'Erro ao registrar usuário administrativo: {str(e)}', 'error')
            return redirect(url_for('admin_bp.register'))

        finally:
            dao.close()

    # Se o método HTTP não for POST (pode ser GET), renderizar o formulário de registro
    return render_template('index.html')

@admin_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        dao = UsuarioAdminDAO()
        try:
            usuario_admin = dao.obter_por_email(email)

            if usuario_admin and usuario_admin.senha == senha:  # Verifica a senha (sem hash)
                session['usuario_id'] = usuario_admin.id
                session['usuario_nome'] = usuario_admin.nome
                session['tipo_usuario'] = 'Administrador'  # Definindo o tipo de usuário como 'Administrador'
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('admin_bp.dashboard'))  # Redireciona para o dashboard após o login

            else:
                flash('Credenciais inválidas. Verifique seu email e senha.', 'error')
                return redirect(url_for('admin_bp.login'))
        except Exception as e:
            flash(f'Erro ao realizar login: {str(e)}', 'error')
            return redirect(url_for('admin_bp.login'))

        finally:
            dao.close()

    # Se o método HTTP for GET, renderize o formulário de login
    return render_template('login_adm.html')


@admin_bp.route('/dashboard')
def dashboard():
    # Verificar se o usuário é administrador
    if 'tipo_usuario' in session and session['tipo_usuario'] == 'Administrador':
        return render_template('./admin/painel.html')
    else:
        flash('Acesso negado.', 'error')
        return redirect(url_for('admin_bp.login'))


@admin_bp.route('/logout')
def logout():
    # Limpar sessão
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('page_bp.index'))
