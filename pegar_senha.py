# Esse arquivo não deve ser utilizado, utilize o arquivo 'main', para rodar o programa

from fabrica_fila import FabricaFila


def pegar_senha():
    fabrica_normal = FabricaFila.pega_fila('normal')
    fabrica_prioritario = FabricaFila.pega_fila('prioritária')

    while True:

        print("""
    1) Fila_normal
    2) Fila_prioritária""")

        opcao = input('\nEm qual fila deseja ir? ').strip()

        if opcao == '1':

            with open('ordem_fila_normal.cvs', encoding='latin_1', mode='a') as arquivo1:

                arquivo1.write('Fila_normal\n')

                fabrica_normal.atualiza_fila()

                print(fabrica_normal.retorna_senha_para_cliente())
                print('=-' *8)

        elif opcao == '2':

            with open('ordem_fila_prioritaria.cvs', encoding='latin_1', mode='a') as arquivo2:

                arquivo2.write('Fila_prioritaria\n')

                fabrica_prioritario.atualiza_fila()

                print(fabrica_prioritario.retorna_senha_para_cliente())

                print('=-' * 8)

        elif opcao == 'encerrar_codigo':
            break

        else:
            print('opção inválida!')
