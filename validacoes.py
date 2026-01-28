from datetime import date

def validar_texto(texto):
    '''
    Função de validação de strings para o contexto dos livros.
    Parametros: Nome do livro.
    '''
    return bool(texto.strip())

def validar_ano(ano):
    """
    Função de validação de inteiros para o contexto dos anos dos livros.
    Parametros: ano
    """
    try:
        ano = int(ano)
    except ValueError:
        return False

    if ano < 1000 or ano > date.today().year:
        return False

    return True