"""
Teste para fluxo basico de app.py
"""


def test_app_eh_criado(app):
    """
    Verifica se o aplicativo foi criado e seu nome está correto.
    """
    assert app.name == "aplicacao.app"


def test_carregamento_do_app_config(config):
    """
    Não devemos rodar os testes com DEBUG ativado.
    """
    assert not config["DEBUG"]
