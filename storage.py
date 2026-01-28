import json
import os

ARQUIVO = 'biblioteca.json'

def carregar_biblioteca():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_biblioteca(biblioteca):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(biblioteca, f, indent=4, ensure_ascii=False)