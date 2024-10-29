from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import relatorio_vendas
    app.register_blueprint(relatorio_vendas)

    return app
