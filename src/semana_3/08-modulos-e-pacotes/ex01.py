from moeda import aumentar, diminuir, metade, dobro, moeda

valor = float(input("Digite o valor: $"))
print(f"A metade de {valor} é {moeda(metade(valor))}")
print(f"O dobro de {valor} é {moeda(dobro(valor))}")
print(f"Aumentando 10% de {valor} temos {moeda(aumentar(valor, 10))}")
print(f"Diminuindo 54% de {valor} temos {moeda(diminuir(valor, 54))}")