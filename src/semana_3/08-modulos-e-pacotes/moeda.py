def aumentar(valor, porc):
    return valor + valor * porc * 0.01

def diminuir(valor, porc):
    return valor - valor * porc * 0.01

def metade(valor):
    return valor/2

def dobro(valor):
    return valor*2

def moeda(valor):
    valor = round(valor, 2)
    return f"R${valor}"
