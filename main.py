from models.biblioteca import Biblioteca
from models.livro import Livro
from validacoes import validar_ano, validar_texto

def menu():
    print("""
1 - Cadastrar livro
2 - Listar livros
3 - Editar livro
4 - Remover livro
0 - Sair
""")

biblioteca = Biblioteca()

while True:
    menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        livro = Livro(id=None, titulo=None, autor=None, ano=None)
        
        while True:
            livro.titulo = input('Digite o titulo do livro: ')
            if validar_texto(livro.titulo):
                break
            else:
                print('\nDigite um título válido!\n')
        while True:
            livro.autor = input('Digite o nome do autor do livro: ')
            if validar_texto(livro.autor):
                break
            else:
                print('\nDigite um autor válido!\n')
        
        while True:
            livro.ano = input('Digite o ano em que o livro foi lançado: ')
            if validar_ano(livro.ano):
                break
            else:
                print('\nDigite um ano válido!\n')
        
        biblioteca.receber_livro(livro)
        print('\nLivro registrado com sucesso!\n')
    elif opcao == '2':
        for livro in biblioteca.lista:
            print(f'''
Id - {livro.id}
Titulo - {livro.titulo}
Autor - {livro.autor}
Ano - {livro.ano}

''')
    elif opcao == '3':
        try:
            escolha_id = int(input('\nDigite o ID do livro que deseja editar: \n'))
        except ValueError:
            print('Digite um ID válido!')
        livro_escolhido = biblioteca.buscar_livro_id(escolha_id)
        print(
        '\nVocê selecionou esse livro: \n'
        f"1. Titulo - {livro_escolhido.titulo}\n"
        f"2. Autor  - {livro_escolhido.autor}\n"
        f"3. Ano    - {livro_escolhido.ano}\n")
        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('Digite um valor correto.')
        if escolha == 1:
            while True:
                novo_titulo = input('Digite o novo titulo: ')
                if validar_texto(novo_titulo):
                    break
                else:
                    print('Digite um ano válido.')
            biblioteca.editar_livro_id(id_=escolha_id, titulo=novo_titulo)
        elif escolha == 2:
            while True:
                novo_autor = input('Digite o novo autor: ')
                if validar_texto(novo_autor):
                    break
                else:
                    print('Digite um autor válido.')
            biblioteca.editar_livro_id(id_=escolha_id, autor=novo_autor)
        elif escolha == 3:
            while True:
                novo_ano = input('Digite o novo ano: ')
                if validar_ano(novo_ano):
                    break
                else:
                    print('Digite um ano válido.')
            biblioteca.editar_livro_id(id_=escolha_id, ano=novo_ano)
        else:
            print('Digite uma opção válida!')      

    elif opcao == '4':
        try:
            escolha_id_remover = int(input('Digite o ID do livro para a deleção: '))
            livro_removido = biblioteca.buscar_livro_id(escolha_id_remover)
        except ValueError:
            print('Digite um valor válido!')
        while True:
            permissao = input(f'Você tem certeza que quer remover o livro {livro_removido.titulo}? (s/n) ')
            if permissao == 's' or permissao == 'n':
                break
            else:
                print('Digite o valor correto. ')
        
        if permissao == 's':
            biblioteca.remover_livro_id(escolha_id_remover)
            print('Livro deletado com sucesso!')
        else:
            print('Livro não deletado!')

    elif opcao == '0':
        break
    else:
        print('Opção inválida.')