from unittest.mock import Mock

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ra.brito@yahoo.com.br',
        'teste de envio',
        'viu deu certo'
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao,):
    usuario = Usuario(nome='Rafael', email='ra.brito@yahoo.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ra.brito@icloud.com',
        'teste de envio',
        'viu deu certo'
    )
    enviador.enviar.assert_called_once_with(
        'ra.brito@icloud.com',
        'ra.brito@yahoo.com.br',
        'teste de envio',
        'viu deu certo'
    )
