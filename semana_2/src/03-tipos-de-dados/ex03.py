"""
    - [ ]  solicite ao usuário o mês do ano no formato numérico 1, 2, 3 ..12 e apresente o nome do ano.
    - Exemplo: entrada 3 saída Março.
    - **Implementar com Dicionário**
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

calendario = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

print(f"O mes {mes} é {calendario.get(mes)}")