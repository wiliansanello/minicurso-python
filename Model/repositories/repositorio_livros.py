from database.connection import DBConnectionHandler
from Model.entities.livro import Livro

class RepositorioLivros:

    def listar(self):
        with DBConnectionHandler() as db:
            return db.session.query(Livro).all()

    def buscar_por_titulo(self, titulo):
        with DBConnectionHandler() as db:
            return db.session.query(Livro)\
                .filter(Livro.titulo.like(f"%{titulo}%"))\
                .all()

    def inserir(self, isbn, titulo, autor, ano):
        with DBConnectionHandler() as db:
            livro = Livro(
                isbn=isbn,
                titulo=titulo,
                autor=autor,
                ano=ano
            )
            db.session.add(livro)
            db.session.commit()
            return livro

    def atualizar(self, isbn, titulo=None, autor=None, ano=None):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.isbn == isbn).first()

            if not livro:
                return None

            if titulo:
                livro.titulo = titulo
            if autor:
                livro.autor = autor
            if ano:
                livro.ano = ano

            db.session.commit()
            return livro

    def deletar(self, isbn):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.isbn == isbn).first()

            if not livro:
                return False

            db.session.delete(livro)
            db.session.commit()
            return True