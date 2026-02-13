tarefas = []
opcao = 0

def mostrar_menu():
    print("Opção 1 - Adicionar tarefas")
    print("Opção 2 - Listar tarefas")
    print("Opção 3 - Marcar tarefa como concluída")
    print("Opção 4 - Sair")

opcao = int(input("Digite uma opção:"))

while opcao != 4:
    mostrar_menu()
    opcao = int(input("Digite uma opção:"))
    
    if opcao == 1:
        nova_tarefa = input("Digite a nova tarefa: ")
        tarefas.append(f"[ ] {nova_tarefa}")

    if opcao == 2:
        if tarefas:
            for listar_tarefas in tarefas:
                print(f"As tarefas são: {listar_tarefas}")
        else:
            print("Não há tarefas.")

    if opcao == 3:
        if tarefas:
            for i, listar_tarefas in enumerate(tarefas, start=1):
                print(f"{i}. {listar_tarefas}")
            numero = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            numero = numero - 1
            if 0 <= numero < len(tarefas):
                tarefa_atual = tarefas[numero]
                tarefa_concluida = tarefa_atual.replace("[ ]", "[X]")
                tarefas[numero] = tarefa_concluida
            else:
                print("Número inválido.")
        else:
            print("Não há tarefas.")

else:
    print("Você saiu do aplicativo de listas de tarefas.")
