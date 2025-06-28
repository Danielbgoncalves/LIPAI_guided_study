"""
- Crie um programa em python que recebe como entrada o comprimento, altura e a largura (cm) de um aquário 
   e calcule as seguintes informações.
- O volume do aquário em litros;
- A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
- A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.
"""

def aquario(aquario_data, temp_desej, temp_amb):
    volume = calc_volume(aquario_data["comprimento"], aquario_data["altura"], aquario_data["largura"])
    pot = calc_pot(volume, temp_desej, temp_amb)
    filt = filtragem(volume)

    return volume, pot, filt
      
    
def calc_volume(comprimento, altura, largura):
    return comprimento * altura * largura

def calc_pot(volume, temp_desej, temp_amb):
    return volume * 0.05 * (temp_desej - temp_amb)

def filtragem(volume):
    return 2.5 * volume

#----------

aquario_data = {
    "comprimento": 0,
    "altura": 0,
    "largura": 0,
}

valores = input("Insira a comprimento, altura e largura: ")
comp, alt, larg = list(map(float, valores.split()))

aquario_data['comprimento'] = comp
aquario_data['altura'] = alt
aquario_data['largura'] = larg

temp_desej = float(input("Insira a temperatura desejada: "))
temp_amb = float(input("Insira a temperatura ambiente: "))

volume, pot, filt = aquario(aquario_data, temp_desej, temp_amb)

print(f"Volume: {volume} \nPotência: {pot} \nFiltragem: {filt}")