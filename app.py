"""
Entrypoint da aplicação Flask.
"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """
    Função que retorna a home
    """
    return "Página inicial da aplicação"
