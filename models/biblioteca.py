import sqlite3
from .livro import Livro

class Biblioteca:
    def __init__(self):
        self.criar_tabela()
    
    def criar_tabela(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS livros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano INTEGER NOT NULL
                )
            """
        )
        conn.commit()
        conn.close()

    def listar_livros(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT * FROM livros
            """
        )
        linhas = cursor.fetchall()
        lista = []
        for linha in linhas:
            livro = Livro(linha[0], linha[1], linha[2], linha[3])
            lista.append(livro)
        conn.close()
        return lista
    
    def receber_livro(self, livro):
        """
        Função para receber livro e adicioná-lo à biblioteca.
        Parametros:
        - Livro: Objeto.
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
                INSERT INTO livros (titulo, autor, ano) VALUES (?, ?, ?)
            """, (livro.titulo, livro.autor, livro.ano)
        )
        conn.commit()
        id = cursor.lastrowid
        conn.close()
        livro.id = id

    def buscar_livro_id(self, id_):
        """
        Função para buscar livros na biblioteca com o id pedido.
        Parametros:
        - Id: Atributo
        """
        conn = self.connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
                SELECT * FROM livros WHERE id = ?
            """, (id_,)
        )

        livro = cursor.fetchone()
        conn.close()

        if livro:
            livro = Livro(livro[0], livro[1], livro[2], livro[3])
            return livro
        return None

    def remover_livro_id(self, id_):
        """
        Função que remove livros da biblioteca com o id pedido.
        Parametros:
        - Id: Atributo
        """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            """
                DELETE FROM livros WHERE id = ?
            """, (id_,)
        )
        conn.commit()
        linha_removida = cursor.rowcount
        conn.close()

        if linha_removida:
            return True
        return False
    
    def editar_livro_id(self, id_, titulo=None, autor=None, ano=None):
        """
        Função que edita livros da biblioteca com o id pedido.
        Atualiza apenas os campos que não forem None.
        Retorna True se o livro foi atualizado, False se o ID não existir.
        """

        campos = []
        valores = []

        if titulo is not None:
            campos.append("titulo = ?")
            valores.append(titulo)

        if autor is not None:
            campos.append("autor = ?")
            valores.append(autor)

        if ano is not None:
            campos.append("ano = ?")
            valores.append(ano)

        # Se nenhum campo foi passado para edição
        if not campos:
            return False

        conn = self.connect_db()
        cursor = conn.cursor()

        sql = f"""
            UPDATE livros
            SET {', '.join(campos)}
            WHERE id = ?
        """

        valores.append(id_)

        cursor.execute(sql, tuple(valores))
        conn.commit()

        atualizado = cursor.rowcount > 0

        conn.close()

        return atualizado

    def connect_db(self):
        return sqlite3.connect('biblioteca.db')

    