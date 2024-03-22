"""
Entrypoint da aplicação Flask.
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/')
def index():
    """
    Função que retorna a home
    """
    return "Página inicial da aplicação"
