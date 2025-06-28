classificacao = {
        (0, 18.5):           "Baixo peso",
        (18.5,  24.9):       "Peso normal",
        (25.0,  29.9):       "Excesso de peso",
        (30.0,  34.9):       "Obesidade de Classe 1",
        (35.0, 39.9):        "Obesidade de Classe 2",
        (40.00, float("inf")):"Obesidade de Classe 3"
    }

def calcular_imc(individuo):
    """ retorna o imc de um indivíduo com base na sua altura e peso """
    peso = individuo.get("peso")
    altura = individuo.get("altura")
    imc =  peso / (altura * altura)
    classificacao = obter_classificacao(imc)
    situacao = situacao_individuo(imc)
    return imc, classificacao, situacao


def obter_classificacao(imc):
    """ retorna a classificação com base no imc """
    for (mini, maxi), categoria in classificacao.items():
        if mini <= imc < maxi:
            return categoria
    


def situacao_individuo(imc):
    """ retorna a situação ('normal', 'perder peso', 'ganhar peso') com base no imc """
    if imc <= 18.5:
        return "ganhar peso"
    elif imc <= 24.9:
        return "normal"
    else:
        return "perder peso"

individuo = {
    "altura": 1,
    "peso": 1
}

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

individuo["altura"] = altura
individuo["peso"] = peso


imc, classi, situacao = calcular_imc(individuo)
print(f"Seu imc: {imc} \nSua classificação: {classi} \nSua situação: {situacao}")