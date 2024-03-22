"""
Fixtures para execução dos testes.
"""
import pytest

from aplicacao.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instância do aplicativo Flask"""
    return create_app()
