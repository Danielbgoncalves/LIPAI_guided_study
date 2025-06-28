"""
    - [ ]  Implemente o `ex03.py` mas ao final do programa deve ser apresentado ao usuário todos os problemas que o identificador informado possui (implementar como list de erros):
    - Ex: identificador informado: B9999999X
        - erros
            - O identificar não inicia com a sequencias ‘BR’
            - O identificador não apresenta números inteiros entre 0001 e 9999
    - Ex: identificador informado: BR9999Y
        - erros
            - O identificar não finaliza com o caracter X
"""

while True:
    codigo = input("Informe seu código: ")
    numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
    errors_msg = []

    is_valid = True
    for i, char in enumerate(codigo, start=0):
        if i == 0 and not char == 'B': 
            is_valid = False
            errors_msg.append("Não tem 'B' como primeiro char")
        if i == 1 and not char == 'R': 
            is_valid = False
            errors_msg.append("Não tem 'R' como segundo char")
        if 1 < i < 6 and char not in numbers: 
            is_valid = False
            errors_msg.append(f"O char {i+1} não é valido nessa posição")
        if i == 6 and not char == 'X': 
            is_valid = False
            errors_msg.append("Não tem 'X' no setimo char")
    
    if is_valid:
        print("Seu código é válido")
    else:
        print("Seu código é inválido pois:")
        for e in errors_msg:
            print("- ", e)
    
