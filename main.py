from storage import carregar_biblioteca
from crud import *

def menu():
    print("""
1 - Cadastrar livro
2 - Listar livros
3 - Editar livro
4 - Remover livro
0 - Sair
""")

biblioteca = carregar_biblioteca()

while True:
    menu()
    opcao = input('Escolha: ')

    if opcao == '1':
        cadastrar_livro(biblioteca)
    elif opcao == '2':
        listar_livros(biblioteca)
    elif opcao == '3':
        editar_livros(biblioteca)
    elif opcao == '4':
        remover_livros(biblioteca)
    elif opcao == '0':
        break
    else:
        print('Opção inválida.')