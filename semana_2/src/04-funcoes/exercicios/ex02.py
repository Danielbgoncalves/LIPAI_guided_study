"""
crie uma função que recebe três números como parâmetro (n1, n2, n3) e retorna a soma dos números
"""


import random

def soma(n1,n2,n3):
    return n1 + n2 + n3

lista = [random.uniform(0,100) for _ in range(3)]
lista =  [round(f,2) for f in lista]
n1,n2,n3 = lista
