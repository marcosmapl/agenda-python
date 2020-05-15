import csv
import model

arquivo_dados = 'contatos.csv'


def salvar_contato(contato):
    with open(arquivo_dados, 'a') as arquivo:
        wt = csv.writer(arquivo)
        wt.writerow(contato)
    print(f'Contato {contato.nome} foi salvo com sucesso!')


def recuper_contatos():
    contatos = []
    with open(arquivo_dados, 'r') as arquivo:
        rd = csv.reader(arquivo)
        for c in map(model.Contato._make, rd):
            contatos.append(c)
    return contatos
