# Esse arquivo não deve ser utilizado, utilize o arquivo 'main', para rodar o programa

from fabrica_fila import FabricaFila


def caixa():

    numero_caixa = int(input('Coloque o número do caixa: '))

    fabrica_normal = FabricaFila.pega_fila('normal')
    fabrica_prioritario = FabricaFila.pega_fila('prioritária')

    contador_prioritario = 0
    contador_normal = 0

    contador_prioritario = atualiza_fila_caixa_prioritario(fabrica_prioritario, contador_prioritario)
    contador_normal = atualiza_fila_caixa_normal(fabrica_normal, contador_normal)

    while True:

        cancelar = int(input("""
1) cliente prioritário
2) cliente normal
3) encerrar caixa

Chamar qual fila?"""))

        if cancelar == 1:

            while True:

                if contador_prioritario > 0:
                    print(fabrica_prioritario.chama_cliente(numero_caixa))

                if contador_prioritario != 0:
                    proximo = input('Chamar proximo?').strip().upper()

                    if proximo == 'N':
                        break
                elif contador_prioritario == 0:
                    print('Não tem mais ninguém na fila prioritária.')
                    break

                contador_prioritario -= 1

        elif cancelar == 2:

            while True:

                if contador_normal > 0:
                    print(fabrica_normal.chama_cliente(numero_caixa))

                if contador_normal != 0:
                    proximo = input('Chamar proximo?').strip().upper()

                    if proximo == 'N':
                        break
                elif contador_normal == 0:
                    print('Não tem mais ninguém na fila normal.')
                    break

                contador_normal -= 1

        elif cancelar == 3:
            break


def atualiza_fila_caixa_prioritario(fabrica_prioritario, contador_prioritario):
    while True:

        with open('ordem_fila_prioritaria.cvs', encoding='latin_1') as arquivo1:

            conte = sum(1 for row in arquivo1)

            for tamanho in range(0, conte):
                fabrica_prioritario.atualiza_fila()

                contador_prioritario += 1
                tamanho += 1

            else:
                break

    return contador_prioritario


def atualiza_fila_caixa_normal(fabrica_normal, contador_normal):
    while True:

        with open('ordem_fila_normal.cvs', encoding='latin_1') as arquivo1:

            conte = sum(1 for row in arquivo1)

            for tamanho in range(0, conte):
                fabrica_normal.atualiza_fila()

                contador_normal += 1
                tamanho += 1

            else:
                break
    return contador_normal


def chamar_cliente_prioritario(numero_caixa, fabrica_prioritario):
    return fabrica_prioritario.chama_cliente(numero_caixa)


def chamar_cliente_normal(numero_caixa, fabrica_prioritario):
    return {fabrica_prioritario.chama_cliente(numero_caixa)}
