from datetime import datetime
import model
import uuid
import parser


def novo_contato():
    print('\n\n -- NOVO CONTATO')
    nome = input('Informe o nome completo: ')
    dt_nasc = input('Informe a data de nascimento: ')
    tel = input('Informe o telefone: ')
    log = input('Informe o logradouro: ')
    cep = input('Informe o cep: ')
    bairro = input('Informe o bairro: ')
    cidade = input('Informe o bairro: ')
    uf = input('Informe o bairro: ')

    contato = model.Contato(
        uuid.uuid4(),
        nome,
        dt_nasc,
        tel,
        log,
        cep,
        bairro,
        cidade,
        uf,
        datetime.now().strftime('%d-%m-%Y'),
        model.__ATIVO
    )

    parser.salvar_contato(contato)


def lista_contatos_ativos():
    contatos = parser.recuper_contatos()

    for contato in contatos:
        if contato.status == 'True':
            print(f'Nome: {contato.nome}')
