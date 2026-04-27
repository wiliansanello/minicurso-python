from flask import Flask, render_template, request, redirect, url_for
from routes.rotas_livro import livros_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(livros_bp, url_prefix="/livros")
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
