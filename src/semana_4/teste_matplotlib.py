from matplotlib import pyplot as plt

###############
#   simples   # 
###############

# Apenas com valores de x e de y 
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