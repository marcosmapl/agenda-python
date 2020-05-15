from collections import namedtuple

__INATIVO = False
__ATIVO = True

Contato = namedtuple(
    'Contato',
    [
        'codigo',
        'nome',
        'data_nascimento',
        'telefone',
        'logradouro',
        'cep',
        'bairro',
        'cidade',
        'uf',
        'data_cadastrado',
        'status'
    ]
)
