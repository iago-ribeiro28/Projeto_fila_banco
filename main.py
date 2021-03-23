import pegar_senha
import caixa


def main():
    usando = 'S'

    while usando == 'S':


        escolha = 0

        while escolha < 1 or escolha < 3:

            print("""
1) usar para o cliente pegar a senha
2) caixa usar para chamar o cliente
3) encerrar programa""")

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
