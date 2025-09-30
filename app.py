from db import get_collection


#-------FUNÇÃO PARA ADICIONAR TAREFA-------
def add_modules():
    collection = get_collection()
    if collection is None:
        return
    
    print("\n--- ADICIONANDO HABILIDADES ---")

    name = input("nome do curso: ")
    tecnology = input("tecnologia usada: ")
    stats = input("status do curso: ")

    while True:
        try:
            progress = int(input("Carga Horária (em horas): "))
            break
        except ValueError:
            print("Valor inválido. Por favor, insira um número inteiro para a carga horária.")

    new_module ={
        "name": name,
        "tecnology": tecnology,
        "stats": stats,
        "progress": progress
    }

    try:
        collection.insert_one(new_module)
        print("\n--- SUCESSO! ---")
        print(f"Módulo '{name}' adicionado com sucesso!")
        print(f"ID gerado com sucesso!")

    except Exception as er:
        print(f"\nErro ao inserir o documento: {er}")

#-------FUNÇÃO PARA MOSTRAR A LISTA-------
def list_modules():

    collection = get_collection()
    if collection is None:
        return
    
    print("\n--- LISTA DE HABILIDADES ---")

    modules = collection.find({})
    found_modules = []

    for module in modules:
        found_modules.append(module)

        name = module.get("name", "N/A")
        tecnology = module.get("tecnology", "N/A")
        status = module.get("stats", "Pendente")
        time = module.get("progress", 0)

        print("-" * 25)
        print(f"  nome do curso: {name}")
        print(f"  tecnologia: {tecnology}")
        print(f"  Status: {status}")
        print(f"  Tempo Gasto: {time}h")
        

    if not found_modules:
        print("Nenhum módulo de estudo rastreado.")
        
    print("-" * 25)
    return found_modules

#-------FUNÇÃO DE ATUALIZAÇÃO-------
def att_modules():

    collection = get_collection()
    if collection is None:
        return
    

    found_modules = list_modules()

    while True:
        try:
            if len(found_modules) == 1:
                print(f"\nApenas um módulo encontrado. Selecionado {found_modules[0]['name']}")

                selected_index = 0
                break
            else:
                print("\n--- QUAL MÓDULO DESEJA ATUALIZAR ---")
                choice = int(input(f"digite um numero entre 1 e {len(found_modules)}: "))

                selected_index = choice -1

                if selected_index>=0 and selected_index<len(found_modules):
                    break
                else:
                    print(f"Escolha inválida. Digite um número entre 1 e {len(found_modules)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    selected_module = found_modules[selected_index]
    module_id = selected_module['_id']

    new_stats = input(f"\nNovo status para '{selected_module['name']}' (Ex: Concluído, Em Pausa): ")

    query = {"_id": module_id}

    att_action = {
        "$set": {
            "stats": new_stats
        }
    }

    try:
        result = collection.update_one(query, att_action)

        print("\n--- SUCESSO! ---")

        if result.matched_count >0:
            print(f"A tarefa '{selected_module['name']}' teve o status atualizado para '{new_stats}'")
        else:
            print("Nenhum documento encontrado com o ID especificado.")
    except Exception as er:
        print(f"\nErro ao atualizar o documento: {er}")

#-------FUNÇÃO PARA DELETAR-------
def del_modules():

    collection = get_collection()
    if collection is None:
        return
    
    found_modules = list_modules()

    while True:
        try:
            if len(found_modules) == 1:

                print(f"Apenas um módulo encontrado. selecionado {found_modules[0]['name']}")
                selected_index = 0
                
                break
            else:
                choice = int(input(f"digite um numero entre 1 e {len(found_modules)}"))

                selected_index = choice -1

                if selected_index>=0 and selected_index<len(found_modules):
                    break
                else:
                    print(f"Escolha inválida. Digite um número entre 1 e {len(found_modules)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    selected_module = found_modules[selected_index]
    module_id = selected_module['_id']

    confirmacao = input(f"Tem certeza que deseja ELIMINAR o módulo '{selected_module['name']}'? (s/n): ").lower()

    if confirmacao != 's':
        print("\nOperação de eliminação cancelada.")
        return
    
    query = {"_id": module_id} 

    try:
        result = collection.delete_one(query)

        print("\n--- SUCESSO! ---")
        if result.deleted_count > 0:
            print(f"Módulo '{selected_module['name']}' eliminado com sucesso!")
        else:
            print("Erro: Nenhum documento foi eliminado (ID não encontrado).")
    except Exception as er:
        print(f"\nErro ao eliminar o documento: {er}")

#-------MENU PRINCIPAL---------
def main_menu():
    """Exibe o menu e controla a navegação do usuário."""
    while True:
        print("\n==================================")
        print("  GERENCIADOR DE ESTUDO E HABILIDADES")
        print("==================================")
        print("1. Adicionar Nova Tarefa (CREATE)")
        print("2. Listar Todas as Tarefas (READ)")
        print("3. Atualizar Status/Tempo (UPDATE)")
        print("4. Excluir Tarefa (DELETE)")
        print("0. Sair")
        print("----------------------------------")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            add_modules()
        elif escolha == '2':
            list_modules()
        elif escolha == '3':
            att_modules()
        elif escolha == '4':
            del_modules()
        elif escolha == '0':
            print("Saindo do gerenciador. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 0 a 4.")

# --- INÍCIO DO PROGRAMA ---
if __name__ == "__main__":
    main_menu()