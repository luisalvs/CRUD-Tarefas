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
            LISTA_TAREFAS = json.load(file)
    else:
        LISTA_TAREFAS = []


def cadastrar_tarefas():
    carregar_json()
    id = int(input('ID: '))
    titulo = input('Digite o nome da tarefa: ').title()
    descricao = input('Descrição: ').title()
    prioridade = input(
        'Qual nível de prioridade BAIXA, MÉDIA ou ALTA? ').title()
    status = input('Status: ').title()

    LISTA_TAREFAS.append({'id': id, 'titulo': titulo, 'descricao': descricao,
                         'prioridade': prioridade, 'status': status})
    criar_json()


def listar_tarefas():
    # Exibe todas tarefas cadastradas
    carregar_json()
    for tarefa in LISTA_TAREFAS:
        print(tarefa)


def atualizar_tarefas():
    # Permite alterar título, descrição, prioridade ou status de uma tarefa existente.
    carregar_json()
    for tarefa in LISTA_TAREFAS:
        print(tarefa)
        tarefa_existente = int(input('Digite o ID da tarefa:  '))
        if tarefa_existente == tarefa['id']:
            print('Digite suas alterações')
            titulo = input('Título: ').title()
            tarefa['titulo'] = titulo
            descricao = input('Descrição: ').title()
            tarefa['descricao'] = descricao
            prioridade = input('Prioridade: ').title()
            tarefa['prioridade'] = prioridade
            status = input('Status: ').title()
            tarefa['status'] = status
            criar_json()
        else:
            print('ID não existe')


def remover_tarefa():
    # Remove uma tarefa pelo id
    carregar_json()
    for tarefa in LISTA_TAREFAS:
        print(tarefa)
        excluir = int(input('Digite o ID da tarefa que deseja excluir: '))
        if excluir == tarefa['id']:
            LISTA_TAREFAS.remove(tarefa)
            criar_json()
        else:
            print('ID não encontrado')
