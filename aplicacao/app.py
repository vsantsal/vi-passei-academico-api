"""
Entrypoint da aplicação Flask.
"""
from flask import Flask


def create_app():
    """
    Fábrica para criar o app principal Flask.
    """
    aplicacao = Flask(__name__)
    return aplicacao


app = create_app()


@app.route('/')
def index():
    """
    Função que retorna a home
    """
    return "Página inicial da aplicação"
