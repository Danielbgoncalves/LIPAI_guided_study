"""
 solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas
"""

v1, v2, v3 = map(int,input("Informe 3 valores: ").split())
media = (v1+v2+v3) / 3
print(f"A média de {v1}, {v2}, {v3} é {media}")