"""
    - [ ]  solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
    - Exemplo: entrada 3 saída Março.
    - **Implementar com Tupla**
"""
entrada_valida = False
while not entrada_valida:
    mes = input("Insira um mês do ano na fomra numérica: ")

    try: 
        mes = int(mes)
        if 1 <= mes <= 12: entrada_valida = True
        else: print ("Insira como número entre 1 e 12 ")

    except TypeError:
        print ("Insira como NÚMERO")
    
    if 0 > mes or mes > 12: entrada_valida = False

calendario = (
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", 
    "Junho", "Julho", "Agosto", "Setembro", "Outubro", 
    "Novembro", "Dezembro"
)

print(f"O mes {mes} é {calendario[mes - 1]}")