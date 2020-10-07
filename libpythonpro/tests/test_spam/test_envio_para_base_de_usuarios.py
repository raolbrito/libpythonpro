import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rafael', email='ra.brito@yahoo.com.br'),
            Usuario(nome='Luiza', email='ra.brito@icloud.com')
        ],
        [
            Usuario(nome='Rafael', email='ra.brito@yahoo.com.br')
        ]
    ]
)
def test_quantidade_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ra.brito@yahoo.com.br',
        'teste de envio',
        'viu deu certo'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
