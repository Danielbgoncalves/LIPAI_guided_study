from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

##############
#  simples   # 
##############

#Apenas com valores de x e de y 
x_values = [1,2,3,4,5,6,7]
y_values_max = [24,26,30,31,34,28,35]
y_values_min = [4,6,3,1,4,4,6]

plt.plot(x_values, y_values_min)
plt.plot(x_values, y_values_max)

plt.show()

# É possível adicionar título e legendas
plt.plot(x_values, y_values_min)
plt.plot(x_values, y_values_max)

plt.title("Mínimas e máximas de cidadolândia")
plt.xlabel("dias da semana")
plt.legend(["Temp. mínima", "Temp. máxima"])

# É possível adicionar estilização nas linhas
plt.plot(x_values, y_values_min, )

#################################
#  múltiplas linhas e colunas   # 
#################################

x = np.linspace(-np.pi, np.pi, 20000)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure("sen vs cos", figsize=(10,5))
plt.subplots_adjust(
    left=0.074,
    right=0.956,
    wspace=0.26
)

axis1 = plt.subplot(1,2,1)
plt.plot(x,y_sin)
axis1.set_title("Seno")

axis2 = plt.subplot(1,2,2)
plt.plot(x,y_cos)
axis2.set_title("Cos")
axis2.set_xlabel("entrada")
axis2.set_ylabel("amplitude")

plt.show()


###############
#  subplots   # 
###############

x = np.arange(0.1, 5, 0.05)
y1 = np.log(x)
y2 = x
y3 = x * np.log(x)
y4 = 2**x

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(8,6))

ax1.plot(x,y1)
ax1.set_title("log(x)")

ax2.plot(x,y2)
ax2.set_title("x")

ax3.plot(x,y3)
ax3.set_title("xlog(x)")

ax4.plot(x,y4)
ax4.set_title("$2^x$")

plt.show()

##################
#  Estilização   # 
##################

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(6,4))
ax1.plot(x,y1, color="#D69A4C", linestyle="dashed", lw=0.8)
ax1.set_title("log(x)")

ax2.plot(x,y2, color="#B373BC", linestyle="dashdot", lw=3)
ax2.set_title("x")

plt.show()

#############################################
#          Exercício do Onboarding          #
#     Usando dados das células tumorais     #
#############################################
df = pd.read_csv("src/semana_4/classification_results_trial_0001.csv", sep=',')

# Crie um gráfico de barras mostrando a contagem de imagens para real_class 
# (quantas "benigno" e "maligno" são na realidade).
plt.figure("Real: malign vs benign")
plt.title("Real: malign vs benign")

x_labels = ["malign", "benign"]

malign_size = ( df["real_class"] == "malign" ).sum()
benign_size = ( df["real_class"] == "benign" ).sum()

plt.bar(x_labels, [malign_size, benign_size], color="#A1E86A", edgecolor="#8BC063", 
        linewidth=2, hatch="*")
plt.show()

# Crie outro gráfico de barras mostrando a contagem de imagens para predicted_class 
# (quantas "benigno" e "maligno" o modelo previu).
plt.figure("Predicted: malign vs benign")
plt.title("Predicted: malign vs benign")

malign_size = ( df["predicted_class"] == "malign" ).sum()
benign_size = ( df["predicted_class"] == "benign" ).sum()

plt.bar(x_labels, [malign_size, benign_size], color="#569AB8", edgecolor="#6385C0", 
        linewidth=2.2, hatch="/")
plt.show()

# Crie um histograma para a coluna prob_benign (probabilidade de ser "benigno")
values = df["prob_benign"].to_numpy()

plt.hist(values, color="#4A93EC", edgecolor="#0A60C8")
plt.show()

# Crie um histograma para a coluna prob_malign (probabilidade de ser "maligno")

values = df["prob_malign"].to_numpy()

plt.hist(values, color="#D6EC4A", edgecolor="#BBC80A")
plt.show()
