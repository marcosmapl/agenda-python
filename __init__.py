import controller

__version__ = '1.0'
__projeto__ = 'Agenda de Contatos CSV'


def main():
    sair = False
    while not sair:
        print('[1] - Cadastrar Novo Contato')
        print('[2] - Lista contatos ativos')
        print('[0] - Sair')
        op = int(input('Digite o número da opção desejada: '))

        if op == 1:
            controller.novo_contato()
        elif op == 2:
            controller.lista_contatos_ativos()
        elif op == 0:
            sair = True


main()
