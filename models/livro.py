class Livro:
    def __init__(self, id, titulo, autor, ano):
        self.id = id
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano": self.ano
        }
    
    @staticmethod
    def from_dict(dados):
        return Livro(
            dados["id"],
            dados["titulo"],
            dados["autor"],
            dados["ano"]
        )
