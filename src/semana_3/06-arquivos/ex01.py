with open("src/semana_3/prontuario.txt", "r") as arq:
    for line in arq:
        print(line)

def carregar_linhas(file_name):
    linhas = []
    with open(f"src/semana_3/{file_name}", "r") as arq:
        for line in arq:
            linhas.append(line.replace("\n", ""))
    
    return linhas

def separar_dados_por_alno(linhas):
    alunos = []
    for aluno in linhas: 
        alunos.append( aluno.split(",") )

    return alunos

def carregar_dados_alunos(file_name):
    linhas = carregar_linhas(file_name)
    dados_alunos = separar_dados_por_alno(linhas) 

    dados = []
    
    for aluno in dados_alunos:
        formato_base = {
		    'prontuario': aluno[0],
		    'nome': aluno[1],
		    'email': aluno[2]
	    }


        dados.append(formato_base)
    
    return tuple(dados)

    
dados = carregar_dados_alunos("prontuario.txt")
print(dados)
