import numpy as np

###############
#    array    # 
###############
                                                                                                                            
arr = np.array([1,2,3,4,5,6])   # cria array do NumPy
np.zeros(2,3)                   # cria array 2 por 3 cheio de zeros
np.ones(4, 1)                   # cria array 4 por 1 cheio de uns
np.full((2,2), 5)               # cria array 2x2 cheio de cincos
np.eye(3)                       # matriz identidade 3x3
np.arange(0, 10, 2)             # array começa em 0 e pula de 2 em 2 até 10 (não incluso)
np.linear(0, 1, 5)              # array começa em 0 até 1 com 5 valores igualmente espaçados

arr.shape                       # retorna uma tupla com o formato
arr.reshape((2,3))              # muda o formato sem mudar os valores 
arr.flatten()                   # achata matriz em array 1D
arr.T                           # trnsposta de uma matriz
np.expand_dims(arr, axis=0)     # adiciona uma dimensão 

np.sum(arr)                     # soma de todos os elementos
np.mean(arr)                    # média
np.std(arr)                     # desvio padrão
np.min(arr) / np.max(arr)       # valor mínimo / máximo
np.argmin(arr) / np.argmax(arr) # indice do valor mínimo / máximo
np.prod(arr)                    # produto de todos os elementos

np.arr > 3                      # array de boleanos
np.where(arr>3, 1, 0)           # [1 if a>3 else 0 for a in arr]
np.any(arr>5)                   # algum valor > 5 ?
np.all(arr>5)                   # todos os valores > 5 ?
arr[arr>3]                      # filtra valores > 3

np.unique(arr)                  # valores únicos
np.sort(arr)                    # ordena valores
np.argsort(arr)                 # ordena índices
np.clip(arr, 2, 4)              # [1,2,3,4,5] -> [2,2,3,4,4]   

###############
#    random   # 
###############

np.ramdom.randint(0,10,(2,3))   # um array no shape(2,3) com inteiros entre 0 e 9
np.random.rand(2,4)             # floats entre 0 e 1 uniformes no formato (2,4)
np.random.rand(4)               # floats entre 0 e 1 normalmente distribuídos (Gausiana)
np.random.uniform(2, 5, size=4) # array com float normalmente distribuídos entre 2 e 5 
np.random.choice([1,2,3], size=1, p=[0.1, 0.7, 0.2]) # escolhe 1 entre o array passado com as probabilidade dadas
np.random.seed(42)              # a partir fixa a aleatoriedade para entradas constantes