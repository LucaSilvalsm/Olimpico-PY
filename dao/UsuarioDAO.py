from Model import db
from Model.Usuario import Usuario

class UsuarioDAO:
    def incluir(self, usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except Exception as e:
            db.session.rollback()
            raise e

    def get_usuario_by_id(self, usuario_id):
        return Usuario.query.get(usuario_id)

    def excluir(self, id):
        usuario = Usuario.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()

    def obter_todos(self):
        return Usuario.query.all()

    def obter_por_email(self, email):
        return Usuario.query.filter_by(email=email).first()

    def close(self):
        db.session.close()
