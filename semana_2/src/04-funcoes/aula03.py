"""
    Ler o artigo a seguir, criar um arquivo aula03.py dentro do diretório src/04-funcoes e 
    escrever os exemplos apresentados no artigo
"""

def world_cup_titles(country, *args):
    print('Country: ', country)
    for y in args:
        print('year: ', y, end="!\n")

world_cup_titles("Brasil", 1987, 1284, 8723, 9763)

def calculate_price(price, **kargs):
    discount = kargs.get('discount')
    tax = kargs.get('tax')
    
    if tax: price *= tax
    if discount: price -= discount

    return price

new_price = calculate_price(100, tax=1.1, discount=5.56)
print(f"{new_price:.2f}")