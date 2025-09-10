from funcoes import cadastrar_tarefas, listar_tarefas, atualizar_tarefas, remover_tarefa

print('LISTA DE TAREFAS DIÁRIAS')

print('''
1 - CADASTRAR TAREFA
2 - LISTAR TAREFA
3 - ATUALIZAR TAREFA
4 - REMOVER TAREFA
5 - Sair
''')

sair = True

while sair:

    opcoes = int(input('Digite uma opção acima: '))

    match opcoes:
        case 1:
            cadastrar_tarefas()
        case 2:
            listar_tarefas()
        case 3:
            atualizar_tarefas()
        case 4:
            remover_tarefa()
        case 5:
            sair = False
