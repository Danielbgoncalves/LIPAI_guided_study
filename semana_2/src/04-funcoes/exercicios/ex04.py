"""
crie uma função que recebe vários argumentos numéricos através do *args retorna a soma dos números
"""

def soma(*args):
    return sum(args)

print("A soma é: ", soma(1,2,3,5,7,9,5,3,5,8,98,4,2,4,5543,2344))

'''
def soma(*args):
    value = 0
    for a in args:
        value += a
    return value
'''