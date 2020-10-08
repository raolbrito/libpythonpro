class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailIvalido(f'Email de remetente invalido: {remetente}')
        return remetente


class EmailIvalido(Exception):
    pass
