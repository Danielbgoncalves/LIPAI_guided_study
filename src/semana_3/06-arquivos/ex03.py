"""
ex03.py com base nos códigos dos exercícios anteriores, crie a função linha_para_dict que recebe uma 
linha do arquivo (string), exemplo SP000001,Maria da Silva,maria@email.com , uma lista com os nomes das 
chaves do dicionário ['prontuario', 'nome', 'email'] e retorna o dicionário correspondente à aquele registro.
Não utilizar bibliotecas ou funções prontas para leitura do arquivo.
"""

def linha_para_dict(linha, colunas):
    itens = [item.strip() for item in linha.split(",")]

    if not len(itens) == len(colunas):
        return None
    
    dictionary = {}
    for i, coluna in enumerate(colunas):
        dictionary[coluna] = itens[i]

    return dictionary

    