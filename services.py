import json
import os

LISTA_TAREFAS = []
filename = 'tarefas.json'


def criar_json():
    with open(filename, 'w') as file:
        json.dump(LISTA_TAREFAS, file, indent=4)


def carregar_json():
    global LISTA_TAREFAS
    if os.path.exists(filename):  # se existir retorna True
        with open(filename) as file:
            json.load(file)
    else:
        LISTA_TAREFAS = []


def cadastrar_tarefa():
    carregar_json()
    id = int(input('ID: '))
    titulo = input('Digite o nome da tarefa: ')
    descricao = input('Descrição: ')
    prioridade = input('Qual nível de prioridade BAIXA, MÉDIA ou ALTA? ')
    status = input('Status: ')

    LISTA_TAREFAS.append({'id': id, 'titulo': titulo, 'descricao': descricao,
                         'prioridade': prioridade, 'status': status})
    criar_json()


def listar_tarefas():
    # Exibe todas tarefas cadastradas
    carregar_json()
    filtro = input('Deseja filtrar por STATUS ou PRIORIDADE: ')
    for tarefa in LISTA_TAREFAS:
        if filtro == 'STATUS':
            print(tarefa['status'])
        else:
            print(tarefa['prioridade'])
