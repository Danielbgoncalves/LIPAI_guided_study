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

# # podemos fazer contas
soma_1931_1960 = df["1931 - 1960"].sum()
media_1961_1990 = df["1961 - 1990"].mean()

print("Soma da coluna 1931 - 1960: ", soma_1931_1960)
print("Media da coluna 1961 - 1990: ", media_1961_1990)

print("="*53)


# # É possível fazer agrupamentos
print ( df.groupby("1991 - 2020") )
# e a partir do agrupamento aplicar contas
# Isso é agrupar aparições de mesma temperatura no intervalo 1991 - 2020 e 
# contar em quantos meses ocorreu a mesma temperatura (exemplo bosta, eu sei)
print ( df.groupby("1991 - 2020")["Category"].count() )

# print("="*53)

# # É possível ordenar o data frame
df.sort_values(by="Category", inplace=True ) # ordem alfabética
print( df )
print("\n")
df.sort_values(by="Category", inplace=True, ascending=False) # ordem descendente
print( df )

#############################################
#          Exercício do Onboarding          #
#     Usando dados das células tumorais     #
#############################################

df = pd.read_csv("src/semana_4/classification_results_trial_0001.csv", sep=',')

### Quantas imagens do conjunto são "benigno" e "maligno"? 

print( df.groupby("real_class")["real_class"].count() ) # Não tá tão equilibrado assim, 45 vs 55

### Identifique em quais imagens o modelo errou a predição 
comparacao = df["real_class"] == df["predicted_class"]
print( comparacao )

### Verifique se o modelo estava confiante mesmo quando errou a predição 

# errou é um vetor com true onde a predição ta errada
errou = df["real_class"] != df["predicted_class"]

# .loc[] devolve onde a condição dele é verdadeira
# .loc[ linhas, colunas ]
print( df[errou].loc[:,["real_class","predicted_class","prob_benign","prob_malign"]] )


### Verdadeiros Positivos (TP) - real maligno, previsto maligno.
df_malign = df[ df["real_class"]  == "malign" ]
true_pos = df_malign["real_class"] == df_malign["predicted_class"]
df_true_pos = df_malign[true_pos]
TP = df_true_pos.shape[0]
print("TP: ",TP)

### Verdadeiros Negativos (TN) - real benigno, previso benigno
df_benign = df[ df["real_class"] == "benign" ]
true_neg = df_benign["real_class"] == df_benign["predicted_class"]
df_true_neg = df_benign[true_neg]
TN = df_true_neg.shape[0]
print("TN: ",TN)

### Falsos Positivos (FP) - real benigno, previsto maligno.
false_pos = df_benign["real_class"] != df_benign["predicted_class"]
df_false_pos = df_benign[false_pos]
FP = df_false_pos.shape[0]
print("FP: ",FP)

### Falsos Negativos (FN) - real maligno, previsto benigno
false_neg = df_malign["real_class"] != df_malign["predicted_class"]
df_false_neg = df_malign[false_neg]
FN = df_false_neg.shape[0]
print("FN: ",FN)


### Acurácia: (TP+TN)/(TP+TN+FP+FN)
print("Acurácia: ", (TP+TN)/(TP+TN+FP+FN) )
### Precisão (Precision): TP/(TP+FP) (relevante para os casos preditos como positivos)
print("Precisão:", TP/(TP+FP) )
### Recall: TP/(TP+FN) (relevante para os casos reais positivos)
print("Recall:", TP/(TP+FN) )
### Especificidade: TN/(TN+FP) (relevante para os casos reais negativos)
print("Especificidade:", TN/(TN+FP) )

### Encontre as 5 imagens "benigno" com a menor probabilidade de serem "benigno" (prob_benign). 
# O que isso pode indicar? 
df_benign.sort_values(by="prob_benign", inplace=True)
print( df_benign.head() )
# Indica que mesmo sendo um caso de tumor malígno a rede deu um falso negativo nos 3 primeiros casos, prob < 0.5
# É um erro que não poderia acontecer em uma aplicação real

### Encontre as 5 imagens "maligno" com a maior probabilidade de serem "benigno" (prob_benign). 
# O que isso pode indicar?

df_malign.sort_values(by="prob_benign", inplace=True, ascending=False)
print( df_malign.head() )
# O modelo tem certeza que se trata de um célula saudável enquanot se trata de uma cancerosa, a certeza é 
# maior que quando confundiu pensando ser cancerosa. Falso negativo