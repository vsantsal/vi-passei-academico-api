"""
Teste para fluxo basico de app.py
"""


def test_app_eh_criado(app):
    """
    Verifica se o aplicativo foi criado e seu nome está correto.
    """
    assert app.name == "aplicacao.app"
