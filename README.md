# Sistema de Biblioteca em Python

Projeto em Python que implementa um sistema de biblioteca em terminal, permitindo cadastrar, listar, editar e remover livros.

---

## Funcionalidades
- Cadastrar livros  
- Listar livros  
- Editar livros  
- Remover livros
- Buscar livros por ID
- Salvar dados automaticamente em JSON  
- Validação de entrada do usuário  
- API REST seguindo padrões HTTP

---

## Tecnologias
- Python 3  
- JSON  
- Flask
---

## Endpoints da API
- Listar todos os livros
```bash 
GET /livros
```

- Buscar livro por ID
```bash 
GET /livros/<id>
```

- Cadastrar novo livro
```bash 
POST /livros
```

Body JSON {

    "titulo": "Duna",
    "autor": "Frank Herbert",
    "ano": 1965

}

- Editar livro
```bash 
PUT /livros/<id>
```

Body JSON {
  "titulo": "Novo título",
  "autor": "Novo autor",
  "ano": 2020
}
Todos os campos são opcionais

- Deletar livro
```bash 
DELETE /livros/<id>
```



## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Luadson/Biblioteca-Python.git
```
2. Entre na pasta do projeto:
```bash
cd Biblioteca-Python
```
3. Instalar dependências:

```bash
pip install flask
```

4. Execute o programa:
```bash
python main.py
```

## Status do projeto
Em desenvolvimento
Versão Atual: v0.3.0

## Autor
José Luadson Araújo Aguiar
Estudante de Python