# Esse arquivo não deve ser utilizado, utilize o arquivo 'main', para rodar o programa

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    fila: list = []

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def retorna_senha_para_cliente(self) -> str:
        return f'Sua senha é {self.senha_atual}'

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}'
