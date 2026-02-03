import json, os
from .livro import Livro
class Biblioteca:
    def __init__(self):
        self.lista = []
        self.arquivo = 'biblioteca.json'
        self.proximo_id = 1
        self.carregar_dados()

    def carregar_dados(self):
        """
        Função feita para carregar dados do JSON
        """
        
        if os.path.exists(self.arquivo):
            self.lista = []
            try:
                with open (self.arquivo, 'r', encoding='utf-8') as f:
                    dados = json.load(f)
                for dicionario in dados['livros']:
                    objeto = Livro.from_dict(dicionario)
                    self.lista.append(objeto)
                self.proximo_id = dados['proximo_id']
            except json.JSONDecodeError:
                self.lista = []
                self.proximo_id = 1

    def salvar_dados(self):
        """
        Função feita para salvar dados para o JSON.
        """
        livros = []
        for objeto in self.lista:
            objeto = objeto.to_dict()
            livros.append(objeto)
        dados_completos = {'proximo_id': self.proximo_id, 'livros': livros}
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, indent=4, ensure_ascii=False)
        


    def receber_livro(self, livro):
        """
        Função para receber livro e adicioná-lo à biblioteca.
        Parametros:
        - Livro: Objeto.
        """
        livro.id = self.proximo_id
        self.lista.append(livro)
        self.proximo_id += 1
        self.salvar_dados()

    def buscar_livro_id(self, id_):
        """
        Função para buscar livros na biblioteca com o id pedido.
        Parametros:
        - Id: Atributo
        """
        for livro in self.lista:
            if livro.id == id_:
                return livro
        return None
    
    def remover_livro_id(self, id_):
        """
        Função que remove livros da biblioteca com o id pedido.
        Parametros:
        - Id: Atributo
        """
        livro = self.buscar_livro_id(id_)
        if livro:
            self.lista.remove(livro)
            self.salvar_dados()
            return True
        return False
    
    def editar_livro_id(self, id_, titulo=None, autor=None, ano=None ):
        """
        Função que edita livros da biblioteca com o id pedido.
        Parametros:
        - Id: Atributo
        - Titulo: Atributo, ou None
        - Autor: Atributo, ou None
        - Ano: Atributo, ou None
        """
        livro = self.buscar_livro_id(id_)
        if livro:
            if titulo is not None:
                livro.titulo = titulo
            if autor is not None:
                livro.autor = autor
            if ano is not None:
                livro.ano = ano
            self.salvar_dados()
            return True
        return False

