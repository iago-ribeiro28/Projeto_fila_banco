# Esse arquivo não deve ser utilizado, utilize o arquivo 'main', para rodar o programa

import abc

from constantes import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    senha_atual: str = ''

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    @abc.abstractmethod
    def retorna_senha_para_cliente(self):
        ...

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abc.abstractmethod
    def atualiza_fila(self):
        ...

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
