"""
    O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência 
    de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.
    Exemplos válidos: BR0001X BR1236X BR9999X; Exemplos inválidos: br0001X BR126X BR99999X BR9999Y; 
    Crie um programa em python que solicita ao usuário um identificador e apresenta se o que foi informado 
    é um valor válido ou inválido.
"""

codigo = input("Informe seu código: ")

# Método masi direto
# numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
# is_valid = False
# for i, char in enumerate(codigo, start=0):
#     if i == 0 and not char == 'B': break
#     if i == 1 and not char == 'R': break
#     if 1 < i < 6 and char not in numbers: break
#     if i == 6 and not char == 'X': break
#     if i == 6: is_valid = True 

#Método mais limpo
is_valid = (
    len(codigo) == 7 and
    codigo.startswith("BR") and
    codigo.endswith("X") and 
    codigo[2:6].isdigit() and
    1 <= int(codigo[2:6]) <= 9999
)



print(f"seu código {'' if is_valid else 'NÃO'} é válido")