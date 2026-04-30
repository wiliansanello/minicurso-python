from flask import Flask
from routes.rotas_livro import livros_bp

def create_app():

    app = Flask(__name__)
    app.register_blueprint(livros_bp, url_prefix="/livros")
    
    @app.route("/")
    def hello():
        return "Use o Postman para testar essa API"

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
