# Para iniciar o programa, o funcionário deverá escolher se aquele terminal
# será usado para o cliente pegar a senha, ou para o caixa chamar os clientes,
#
# Se o cliente for pegar a senha, o programa ficará rodando até que o funcionário
# vá encerrar o programa escrevendo "encerrar_codigo"

import pegar_senha
import caixa


def main():
    usando = 'S'

    while usando == 'S':


        escolha = 0

        while escolha < 1 or escolha < 3:

            print("""
1) Caixa usar para chamar o cliente;
2) Usar para o cliente pegar a senha;
3) Encerrar programa.""")

            escolha = int(input('Escolha uma opção: '))

            if escolha == 1:
               caixa.caixa()
            elif escolha == 2:
                pegar_senha.pegar_senha()
            elif escolha == 3:
                break

        if escolha == 3:
            break
        else:
            usando = input('Gostaria de reiniciar o programa? [S/N]').strip().upper()


main()
