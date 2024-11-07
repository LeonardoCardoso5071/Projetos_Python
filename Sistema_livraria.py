# Mensagem de boas-vindas
print("Bem-vindo a Livraria do Leonardo Cardoso")

# Lista vazia para armazenar os livros
lista_livro = []
# Variável global para controle do id
id_global = 0

# Função para cadastrar um livro
def cadastrar_livro(id): # Receber o id como parâmetro
    global id_global # Avisar que a variável é global
    print("-------------------------------------------") # Separador
    print("---------- MENU CADASTRAR LIVRO -----------") # Menu de cadastro
    nome = input("Digite o nome do livro: ") # Solicitar os dados do livro
    autor = input("Digite o nome do autor: ") # Solicitar os dados do livro
    editora = input("Digite o nome da editora: ") # Solicitar os dados do livro
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora} # Dicionário com os dados do livro
    lista_livro.append(livro) # Adicionar o livro na lista
    id_global += 1 # Incrementar o id
    print("Livro cadastrado com sucesso.") # Mensagem de sucesso

# Função para consultar livros
def consultar_livro(): # Sem parâmetros
    while True: # Loop para o menu de consulta
        print("-------------------------------------------") # Separador
        print("---------- MENU CONSULTAR LIVRO -----------") # Menu de consulta
        print("1 - Consultar Todos os livros") # Opções de consulta
        print("2 - Consultar por Nome do Livro") # Opções de consulta
        print("3 - Consultar por Nome do Autor") # Opções de consulta
        print("4 - Consultar por Nome da Editora") # Opções de consulta
        print("5 - Consultar por ID") # Opções de consulta
        print("6 - Retornar ao menu") # Opções de consulta
        opcao = input("Escolha uma opção: ").lower()  # Converter para minúsculas
        if opcao == '1': # Consultar todos os livros
            print("\nLista de Livros:") # Mostrar todos os livros
            for livro in lista_livro: # Percorrer a lista de livros
                print(f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n") # Mostrar os dados do livro
        elif opcao == '2': # Consultar por nome do livro
            nome_busca = input("Digite o nome do livro: ").lower()  # Converter para minúsculas
            print("Livros com o nome", nome_busca + ":") # Mostrar os livros com o nome
            for livro in lista_livro: # Percorrer a lista de livros
                if livro['nome'].lower() == nome_busca:  # Converter para minúsculas
                    print(f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n") # Mostrar os dados do livro
        elif opcao == '3': # Consultar por nome do autor
            autor_busca = input("Digite o nome do autor: ").lower()  # Converter para minúsculas
            print("Livros do autor", autor_busca + ":") # Mostrar os livros do autor
            for livro in lista_livro: # Percorrer a lista de livros
                if livro['autor'].lower() == autor_busca:  # Converter para minúsculas
                    print(f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n") # Mostrar os dados do livro
        elif opcao == '4': # Consultar por nome da editora
            editora_busca = input("Digite o nome da editora: ").lower()  # Converter para minúsculas
            print("Livros da editora", editora_busca + ":") # Mostrar os livros da editora
            for livro in lista_livro: # Percorrer a lista de livros
                if livro['editora'].lower() == editora_busca:  # Converter para minúsculas
                    print(f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n") # Mostrar os dados do livro
        elif opcao == '5': # Consultar por ID
            id_busca = int(input("Digite o ID do livro: ")) # Solicitar o ID
            for livro in lista_livro: # Percorrer a lista de livros
                if livro['id'] == id_busca: # Se encontrar o livro
                    print(f"ID: {livro['id']}\nNome: {livro['nome']}\nAutor: {livro['autor']}\nEditora: {livro['editora']}\n") # Mostrar os dados do livro
                    break # Se encontrar o livro
            else: # Se não encontrar o livro
                print("Livro não encontrado.") # Se não encontrar o livro
        elif opcao == '6': # Retornar ao menu
            break # Sair do loop
        else: # Opção inválida
            print("Opção inválida.") # Mensagem de erro

# Função para remover um livro
def remover_livro(): # Sem parâmetros
    print("-------------------------------------------") # Separador
    print("---------- MENU REMOVER LIVRO ------------") # Menu de remoção
    print("Lista de Livros:") # Mostrar todos os livros
    for livro in lista_livro: # Percorrer a lista de livros
        print(f"ID: {livro['id']}, Nome: {livro['nome']}") # Mostrar os dados do livro
    id_remover = int(input("\nDigite o ID do livro a ser removido: ")) # Solicitar o ID
    for livro in lista_livro: # Percorrer a lista de livros
        if livro['id'] == id_remover: # Se encontrar o livro
            lista_livro.remove(livro) # Remover o livro
            print("Livro removido.") # Mensagem de sucesso
            break # Se encontrar o livro
    else: # Se não encontrar o livro
        print("ID inválido.") # Mensagem de erro

# Menu principal
while True: # Loop para o menu principal
    print("-------------------------------------------") # Separador
    print("------------- MENU PRINCIPAL --------------") # Menu principal
    print("1 - Cadastrar Livro") # Opções do menu
    print("2 - Consultar Livro(s)") # Opções do menu
    print("3 - Remover Livro") # Opções do menu
    print("4 - Sair") # Opções do menu
    opcao_menu = input("Escolha a opcao desejada: ").lower()  # Converter para minúsculas
    if opcao_menu == '1': # Cadastrar livro
        cadastrar_livro(id_global) # Chamar a função de cadastro
    elif opcao_menu == '2': # Consultar livros
        consultar_livro() # Chamar a função de consulta
    elif opcao_menu == '3': # Remover livro
        remover_livro() # Chamar a função de remoção
    elif opcao_menu == '4': # Sair
        print("Encerrando o programa...") # Mensagem de encerramento
        break # Sair do loop
    else: # Opção inválida
        print("Opção inválida.") # Mensagem de erro
