from validacoes import validar_texto, validar_ano
from storage import salvar_biblioteca

def buscar_livro_id(id, biblioteca):
    for livro in biblioteca:
        if livro['id'] == id:
            return livro
    return None

def cadastrar_livro(biblioteca):
    """
    Função necessária para cadastrar os livros na lista biblioteca do sistema!
    Requisitos: 
    - Autor
    - Título
    - Ano
    - Id
    - Adicionado a biblioteca
    """
    while True:
        titulo_livro = input('Digite o título do livro: ')
        if validar_texto(titulo_livro):
            break
        else:
            print('Titulo inválido. Tente novamente.\n')
    

    while True:
        autor_livro = input('Digite o autor do livro: ')
        if validar_texto(autor_livro):
            break
        else:
            print('Autor Inválido. Tente novamente.')

    while True:
        ano_livro = input('Digite o ano que o livro foi lançado: ')
        if validar_ano(ano_livro):
            break
        else:
            print('Ano Inválido! Tente novamente')
    id_livro = len(biblioteca) + 1

    livro = {'titulo': titulo_livro, 'autor': autor_livro, 'ano': ano_livro, 'id': id_livro}
    biblioteca.append(livro)
    salvar_biblioteca(biblioteca)


def listar_livros(biblioteca):
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


def editar_livros(biblioteca):
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
        return
    
    livro = buscar_livro_id(id_pedido, biblioteca)
    if livro is None:
        print('Livro não encontrado!')
        return
    
    print(
        '\nVocê selecionou esse livro: \n'
        f"1. Titulo - {livro['titulo']}\n"
            f"2. Autor - {livro['autor']}\n"
            f"3. Ano - {livro['ano']}\n")
    try:
        escolha = int(input('Escolha uma opção: '))
    except ValueError:
        print('Digite uma opção válida.')
        return
    if escolha == 1:
        while True:
            titulo_novo = input('Digite um novo titulo para o livro: ')
            if validar_texto(titulo_novo):
                livro['titulo'] = titulo_novo
                break
            print('Titulo Inválido. Tente novamente.')
        
        salvar_biblioteca(biblioteca)
        print(f'\nVocê trocou o titulo para {livro['titulo']}!\n')
        return
    elif escolha == 2:
        while True:
            autor_novo = input('Digite um novo autor para o livro: ')
            if validar_texto(autor_novo):
                livro['autor'] = autor_novo
                break
            print('Autor Inválido. Tente novamente.')
        
        salvar_biblioteca(biblioteca)
        print(f'\nVocê trocou o autor para {livro['autor']}!\n')
        return
    elif escolha == 3:
        while True:
            ano_novo = (input('Digite um novo ano para o livro: '))
            if validar_ano(ano_novo):
                livro['ano'] = ano_novo
                break
            print('Ano Inválido! Tente novamente!')
        
    else:
        print('Digite um valor válido. ')
        return
    
    salvar_biblioteca(biblioteca)
    print(f'\nVocê trocou o ano para {livro['ano']}!\n')
    return
    

def remover_livros(biblioteca):
    """
    Função feita para remover livros da lista
    Pede ID do livro ao usuario
    Percorre a lista biblioteca
    Deve remover o livro da lista
    Encerrar a função. 
    """
    if len(biblioteca) == 0:
        print('\nNão há livros para serem deletados! \n')
        return
    else:
        try:
            id_pedido = int(input('Digite o ID do livro para deleção: '))
        except ValueError:
            print('Digite um id válido.')
            return

        livro = buscar_livro_id(id_pedido, biblioteca)
        if livro is None:
            print('\nLivro não encontrado.\n')
            return
        
        autorizacao = input('\nVoce tem certeza? (s/n)\n')
        if autorizacao == 's':
            biblioteca.remove(livro)
            salvar_biblioteca(biblioteca)
            print(f'\nO livro {livro['titulo']} foi deletado da lista!\n')
        elif autorizacao == 'n':
            return
        else:
            print('Digite apenas (s ou n)')
            return
        

