from flask import Blueprint, jsonify, request
from Model.repositories.repositorio_livros import RepositorioLivros

livros_bp = Blueprint("livros", __name__)
repo = RepositorioLivros()

#GET para todos os livros
@livros_bp.route("/", methods=["GET"])
def listar_livros():
    livros = repo.listar()

    return jsonify([
        {
            "isbn": l.isbn,
            "titulo": l.titulo,
            "autor": l.autor,
            "ano": l.ano
        } for l in livros
    ])

#GET por título
@livros_bp.route("/buscar", methods=["GET"])
def buscar():
    titulo = request.args.get("titulo", "")
    livros = repo.buscar_por_titulo(titulo)

    return jsonify([
        {
            "isbn": l.isbn,
            "titulo": l.titulo,
            "autor": l.autor,
            "ano": l.ano
        } for l in livros
    ])

#POST - Insere um novo livro
@livros_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()

    livro = repo.inserir(
        isbn=data["isbn"],
        titulo=data["titulo"],
        autor=data["autor"],
        ano=data["ano"]
    )

    return jsonify({"msg": "Livro criado", "isbn": livro["isbn"]}, 201)

#PUT - Altera informações do livro
@livros_bp.route("/<int:isbn>", methods=["PUT"])
def atualizar(isbn):
    data = request.get_json()

    livro = repo.atualizar(
        isbn,
        data.get("titulo"),
        data.get("autor"),
        data.get("ano")
    )

    if not livro:
        return jsonify({"erro": "Livro não encontrado"}), 404

    return jsonify({"msg": "Atualizado com sucesso"})

@livros_bp.route("/<int:isbn>", methods=["DELETE"])
def deletar(isbn):
    ok = repo.deletar(isbn)

    if not ok:
        return jsonify({"erro": "Livro não encontrado"}), 404

    return jsonify({"msg": "Deletado com sucesso"})