"""
    solicite ao usuário 3 números, armazene esses elementos em uma lista e apresente no final o menor e 
    maior elemento
"""

values = input("Informe 3 números: ")
values = list(map(int, values.split()))

print(f"Os valores são: {values}. \nO menor: {min(values)} \nO maior: {max(values)}")