import pandas as pd

# Abrir um arquivo, aparentemente, por padrão usa a vírgula como separador,
# da pra deixar a ; como usando sep
df = pd.read_csv("src/semana_4/temp_max_BH.csv", sep=";")

# head() mostra as 5 primeiras linhas
print( df.head() )

print("="*53)

# tail() mostra aas 5 ultimas linhas
# Continua mostrando a primeira linha, considera ela como uma cabeçalho
print( df.tail() )

print("="*53)

# Pode mostrar apenas colunas específicas, sem o cabeçalho
# Temperatura média de BH entre 1931 e 1960, por exemplo
print( df["1931 - 1960"].tail() )

print("="*53)

# O cabeçalho como fizemos não é parte dos dados, é parte da estrutura
# se quisessemos que ele fosse parte dos dados deveria carregar passando o parametro
# header=None no pd.read_cvs(..., header=None)
# Para retira-lo agora podemos fazer:

matriz = df.values # o retorno é uma matriz numpy, perde os métodos do pandas

df_sem_cabeçalho = pd.DataFrame(df.values) # ainda possui propriedades de Data Frame

print("="*53)

# Adicionar uma nova linha
# pode ser feito de duas formas, se ja sabemos o indice:
df.loc[13] = ["MesNovo", 0, 100, 32.4]

# ou se não souber a linha e quiser adicionar no fim:
new_line = pd.DataFrame([["MesNovíssimo", 0, 50, 12.4]], columns=["Category","1931 - 1960","1961 - 1990","1991 - 2020"])
df = pd.concat([df, new_line], ignore_index=True)

print( df )

print("="*53)

# Para apagar uma linha
new_df = df.drop(13) # A mudança fica no df novo
df.drop([12,13], inplace=True) # A mudança já fica no atual

print( df )

print("="*53)

# O separados pra casasa decimais padrão é o ".", aqui usamos ","
# podemos trocar em todo o arquivo
colunas = ["1931 - 1960","1961 - 1990","1991 - 2020"]
for col in colunas:
    df[col] = df[col].str.replace(',','.')

# Seria mais fácil já definir a virgula como esse separador desde o início
# isso pode ser feito colocando decimal="," na hora de abrir o arquivo
# df = pd.read_csv(..., decimal=",")

print( df )

print("="*53)

# Converter str para números
for col in colunas:
    df[col] = df[col].astype(float)

print( df )

print("="*53)

# podemos fazer contas
soma_1931_1960 = df["1931 - 1960"].sum()
media_1961_1990 = df["1961 - 1990"].mean()

print("Soma da coluna 1931 - 1960: ", soma_1931_1960)
print("Media da coluna 1961 - 1990: ", media_1961_1990)

print("="*53)


# É possível fazer agrupamentos
print ( df.groupby("1991 - 2020") )
# e a partir do agrupamento aplicar contas
# Isso é agrupar aparições de mesma temperatura no intervalo 1991 - 2020 e 
# contar em quantos meses ocorreu a mesma temperatura (exemplo bosta, eu sei)
print ( df.groupby("1991 - 2020")["Category"].count() )

print("="*53)

# É possível ordenar o data frame
df.sort_values(by="Category", inplace=True ) # ordem alfabética
print( df )
print("\n")
df.sort_values(by="Category", inplace=True, ascending=False) # ordem descendente
print( df )