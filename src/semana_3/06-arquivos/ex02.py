"""
ex02.py crie a função carregar_dados_projetos que recebe como parâmetro o nome de um arquivo que contém dados 
de projetos e retorna uma tupla, onde cada elemento é um dicionário com as seguintes chaves: codigo 
(número inteiro que representa o código do projeto), titulo e responsável (nome do professor responsável pelo 
projeto). Não utilizar bibliotecas ou funções prontas para leitura do arquivo.
"""

def carrega_linhas(file_name):
    linhas = []
    with open(f"src/semana_3/{file_name}", "r") as arq:
        for line in arq:
            linhas.append(line.replace("\n",""))

    return linhas


def carregar_dados_projetos(file_name):
    linhas = carrega_linhas(file_name)
    dados = []
    for linha in linhas:
        linha = linha.split(",")
        dados.append(
            {
                "codigo": linha[0],
                "titulo": linha[1],
                "responsavel": linha[2]
            }
        )

    return tuple(dados)

dados = carregar_dados_projetos("projeto.txt")

print(dados)
