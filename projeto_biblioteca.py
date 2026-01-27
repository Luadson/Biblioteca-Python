"""
Temos essas funcionalidades:
Cadastrar livro.
Listar livros.
Editar livros.
Remover livros.
Sair do sistema.
"""
biblioteca = []

def mostrar_menu():
    print(
    "===== SISTEMA DE BIBLIOTECA =====\n"
    "1 - Cadastrar livro\n"
    "2 - Listar livros\n"
    "3 - Editar livro\n"
    "4 - Remover livro\n"
    "0 - Sair\n"
    "==============================="
    )

def cadastrar_livro():
    """
    Função necessária para cadastrar os livros na lista biblioteca do sistema!
    Requisitos: 
    - Autor
    - Título
    - Ano
    - Id
    - Adicionado a biblioteca
    """
    titulo_livro = input('Digite o título do livro: ')
    autor_livro = input('Digite o autor do livro: ')
    ano_livro = int(input('Digite o ano que o livro foi lançado: '))
    id_livro = len(biblioteca) + 1

    livro = {'titulo': titulo_livro, 'autor': autor_livro, 'ano': ano_livro, 'id': id_livro}
    biblioteca.append(livro)


def listar_livros():
    """
    Função necessária para percorrer a lista de livros.
    Mostrar:
    - ID
    - Titulo
    - Autor
    - Ano
    """
    if len(biblioteca) == 0:
        print('\nNenhum livro cadastrado.\n')
    for livro in biblioteca:
        print(f'\nID: {livro['id']}\n'
              f'Titulo: {livro['titulo']}\n'
              f'Autor: {livro['autor']}\n'
              f'Ano: {livro['ano']}\n')


def editar_livros():
    """
    Função feita para editar livros na lista baseado no ID dado.
    Deve ver se biblioteca esta vazia
    Pede ID ao usuario
    Percorre a lista de biblioteca
    Edita titulo, autor ou ano
    Mostrar mensagem de sucesso
    Encerrar função
    """
    if len(biblioteca) == 0:
        print('\nA biblioteca está vazia!\n')
        return
    try:
        id_pedido = int(input('Digite o ID para edição: '))
    except ValueError:
        print('\nDigite um ID válido. \n')
    
    for livro in biblioteca:
        if id_pedido == livro['id']:
            print('\n Você selecionou esse livro: \n'
                  f'1. Titulo - {livro['titulo']}\n'
                  f'2. Autor - {livro['autor']}\n'
                  f'3. Ano - {livro['ano']}\n')
            escolha = int(input('Escolha uma opção: '))
            if escolha == 1:
                titulo_novo = input('Digite um novo titulo para o livro: ')
                livro['titulo'] = titulo_novo
                return
            elif escolha == 2:
                autor_novo = input('Digite um novo autor para o livro: ')
                livro['autor'] = autor_novo
                return
            elif escolha == 3:
                try:
                    ano_novo = int(input('Digite um novo ano para o livro: '))
                except ValueError:
                    print('Digite um valor válido.')
                    return
                livro['ano'] = ano_novo
                return
            else:
                print('Digite um valor válido. ')
                return
        


def remover_livros():
    """
    Função feita para remover livros da lista
    Pede ID do livro ao usuario
    Percorre a lista biblioteca
    Deve remover o livro da lista
    Encerrar a função. 
    """
    encontrado = False
    if len(biblioteca) == 0:
        print('\nNão há livros para serem deletados! \n')
    else:
        try:
            id_pedido = int(input('Digite o ID do livro para deleção: '))
        except ValueError:
            print('Digite um id válido.')

        for livro in biblioteca:
            if livro['id'] == id_pedido:
                biblioteca.remove(livro)
                print(f'\nO livro {livro['titulo']} foi deletado da lista!\n')
                encontrado = True
                return
            if encontrado == False:
                print('\nLivro não encontrado.\n')

while True:
    mostrar_menu()
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite apenas numeros!\n')
        continue
    if opcao == 1:
        cadastrar_livro()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        editar_livros()
    elif opcao == 4:
        remover_livros()
    elif opcao == 0:
        print('Programa Encerrado.')
        break
    else:
        opcao = print('Digite uma opção válida! ')