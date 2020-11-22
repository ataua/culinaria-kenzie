from environs import Env
import csv

env = Env()
env.read_env()

def listar_receitas():

    with open(env('RECEITAS_CSV')) as f:
        reader = csv.DictReader(f)
        receitas = [receita for receita in reader]

        for receita in receitas:
            receita['descricao'] = receita['descricao'].replace('*virgula*', ',')

    return receitas


def buscar_receita(termo):
    receitas = listar_receitas()
    # print(receita in receita for receitas)
    return [receita for receita in receitas if termo in receita['nome']]
    