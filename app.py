from flask import Flask, jsonify, request
from models.biblioteca import Biblioteca
from models.livro import Livro
from validacoes import validar_ano, validar_texto


app = Flask(__name__)
biblioteca = Biblioteca()

@app.route('/livros', methods=['GET'])
def listar_livros():
    lista_nova = []
    for livro in biblioteca.lista:
        livro = livro.to_dict()
        lista_nova.append(livro)
    return jsonify(lista_nova), 200

@app.route('/livros/<int:id>', methods=['GET'])
def mostrar_livro(id):
    livro = biblioteca.buscar_livro_id(id)
    if livro:
        return jsonify(livro.to_dict()), 200
    else:
        return jsonify({'erro': 'Livro não encontrado!'}), 404

@app.route('/livros', methods=['POST'])
def novo_livro():
    dados = request.json
    if dados is not None:
        titulo = dados.get('titulo')
        if titulo:
            if not validar_texto(titulo):
                return jsonify({'erro': 'Dados inválidos'}), 400
        else:
            return jsonify({'erro': 'Dados inválidos'}), 400
        autor = dados.get('autor')
        if autor:
            if not validar_texto(autor):
                return jsonify({'erro': 'Dados inválidos'}), 400
        else:
            return jsonify({'erro': 'Dados inválidos'}), 400
        try:
            ano = int(dados.get('ano'))
        except ValueError:
            return jsonify({'erro': 'Valor inválido'}), 400
        if not validar_ano(ano):
            return jsonify({'erro': 'Dados inválidos'}), 400
        livro = Livro(id=None, titulo=titulo, autor=autor, ano=ano)
        biblioteca.receber_livro(livro)
        livro = livro.to_dict()
        return jsonify({'livro registrado': livro}), 201

    else:
        return jsonify({'erro': 'Json não encontrado'}), 400
    
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    dados = request.json

    if dados is None:
        return jsonify({'erro':'Json não encontrado.'}), 400


    titulo = dados.get('titulo')
    autor = dados.get('autor')
    ano = dados.get('ano')
    
    if titulo is None and autor is None and ano is None:
        return jsonify({'erro': 'Valor inválido'}), 400

    
    if titulo != None:
        if validar_texto(titulo) is False:
            return jsonify({'erro':'Valor inválido.'}), 400
        
    if autor != None:
        if validar_texto(autor) is False:
            return jsonify({'erro':'Valor inválido.'}), 400
        
    if ano != None:
        try:
            ano = int(ano)
        except ValueError:
            return jsonify({'erro: Valor inválido.'}), 400
        if validar_ano(ano) is False:
            return jsonify({'erro': 'Valor inválido.'}), 400
        
    livro = biblioteca.buscar_livro_id(id)
    if livro is None:
        return jsonify({'erro': 'ID Inexistente'}), 404
    livro = livro.to_dict()

    biblioteca.editar_livro_id(id, titulo=titulo, autor=autor, ano=ano)
    

    return jsonify({'Livro editado': livro}), 200

    
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    delecao = biblioteca.remover_livro_id(id)

    if delecao is False:
        return jsonify({'erro':'Livro não existe!'}), 404
    else:
        return '', 204


app.run()