import pytest
from libpythonpro.spam.enviador_de_email import Enviador, EmailIvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['ra.brito@yahoo.com.br', 'raolbrito@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'ra.brito@icloud.com',
        'se liga no tom',
        'Teste do monstrão saindo da jaula.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'raolbrito']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailIvalido):
        enviador.enviar(
            destinatario,
            'ra.brito@icloud.com',
            'se liga no tom',
            'Teste do monstrão saindo da jaula.'
        )
