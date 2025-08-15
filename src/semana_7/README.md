Respostas para exercícios da semana 7 do Onboarding da LIPAI
UFU - Agosto, 2025

Usando [colab](https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/main/notebooks/Aula_18_b_Redes_Neurais_com_PyTorch.ipynb#scrollTo=cPGWImC2wKMo) do Profs. Storopoli & Souza como referência

#  Redes Neurais Artificiais e PyTorch

##### 1 - Com base no material apresentado no notebook, o que é uma função de ativação (como a ReLU)? Por que normalmente usamos entre as camadas?
Funções de ativação ocorrem em cada neurônio após cada cálculo da sua soma ponderada (produto escalar entre entradas e pesos mais bias), isso ocorre para que haja quebra da linearidade, sem ela, mesmo que várias camdas fossem empilhadas seriam equivalentes a uma única camada linear.  
Essa funções permitem que contornor mais precisos possam ser traçados entre as features de modo a determinar melhor a classificação do modelo, sem essa técnica, apenas relações lineares, como E-lógicos e OU-lógicos poderiam ser realizados, para relações mais complexas como XOR é necessário modelos que apliquem ativações em suas camadas internas.

---

##### 2 -  Explique o que cada uma das seguintes linhas de código faz e por que ela é necessária:
**1. model.train()**
model.train() prepara o modelo para treinamento, isto é, permitir que o pesos e bias dos neurônios adaptáveis sejam atualizados pelo backpropagation, além disso, camadas como nn.Dropout e nn.BatchNorm passam a operar de modo especial. 
*nn.Dropout(p=0.2)* é um objeto utilizado pelo modelo para zerar valores de seus neurônios internos, cada um tem p chance de ser zerado. Isso ocorre para que o modelo não fique dependente de todos os seus neurônios para a predição, forçandos todos a funcionarem bem juntos. Reduzindo, também, o risco de overfiting. 
*nn.BatchNorm(n)* é outro objeto, serve para normalizar saídas internas das camadas durante o forward, garante maior velocidade de treinamento e permite maior learning_rate. 'n' é o númeor de features que será interpretada como uma unidade na normalização, em tabelas n=1, em imagens de 3 canais n=3, se tratar-se de uma sída de convolução com mapas de tamanho 32, n=32. No modo treinamento a normalização depende dos valores de seu batch, se em avaliação média e desvio global são considerados já que normalmente, nesses casos, os batchs são pequenos demais e sua média e desvio poderiam ser pouco representativos. 

**2. optimizer.step()**
- `optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)`
optimizer é um objeto com uma política de avaliação específica, nesse caso Adam. `model.parameters()` é os parâmetros do modelo e `lr` é a taxa com que o modelo aprende, quanto maior mais rápido os parametros mudam.
- `loss.backward()` analisa o grafo gerado pelo forward e retorna os valores novos para os parametros na direção de minimizar a função de custo, isto é, contra a dereivada da função.
- optimizer.step() analisa cada gradiente de cada neurônio e atualiza os valores do tensor utilizando a regra escolhida, por exemplo, se for SGD: param.data -= lr_rate * param.grad.
O que ele faz é dar uma passo extra na direção que minimiza o custo da rede. A cada forward, há um backpropagation e um step, com várias iterações a tendência é alcançar um ótimo local no função de perda.

**3. Qual a diferença fundamental entre os modos model.train() e model.eval()?**
Em train o modelo permite que os pesos dos neurônios sejam ajustáveis, utiliza de normalização entre camadas internas usando de medidas do batch de treinamento e permite dropouts em neurônios internos, já na fase de avaliação os pesos estão travados, a normalização das ativações é com base em média e desvio médios das seções de treino e não há dropout algum.   

---

##### 3 - Modifique a classe ClassBin para que a rede tenha a seguinte arquitetura:

**a. Camada de Entrada: Mantém as 4 features de entrada.**
``` python
class ClassBin(nn.Module):
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 20)  # Entra 4 features sai 20
        self.fc2 = nn.Linear(20, 1)  # entra 20 sai uma ativação
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.sigmoid(x)
        return x

model = ClassBin()
```

**b. Primeira Camada Oculta: nn.Linear com 4 neurônios de entrada e 16 neurônios de saída, seguida por uma ativação ReLU.**
``` python
class ClassBin(nn.Module):
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 16)  # 1° camada oculta: 16 neurônios
        self.fc2 = nn.Linear(16, 1)  # Camada de saída
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.sigmoid(x) # Não foi pedido mas ta aqui mesmo asism
        return x

model = ClassBin()
```
1. A rede possui uma camada de entrada de 4 neurônios que enviará suas ativações para a primeira camada oculta, que possui 16 neurônios.
2. Na linha `x = F.relu(self.fc1(x))` há uma ReLu que é a ativação dessa primeira camada oculta
3. A próxima camada é a de saída com 1 neurônio

**c. Segunda Camada Oculta: nn.Linear com 16 neurônios de entrada e 8 neurônios de saída, seguida por uma ativação ReLU.**
``` python
class ClassBin(nn.Module):
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 16)  # 1° camada oculta: 16 neurônios
        self.fc2 = nn.Linear(16, 8)  # Camada de saída / ele ta chamando isso aqui de segunda camada oculta tb
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.sigmoid(x) # Não foi pedido mas ta aqui mesmo asism
        return x

model = ClassBin()
```

**d. Camada de Saída: nn.Linear com 8 neurônios de entrada e 1 neurônio de saída, seguida por uma ativação Sigmoid.**
``` python
class ClassBin(nn.Module):
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 16)  # 1° camada oculta: 16 neurônios
        self.fc2 = nn.Linear(16, 8)  # 2° camada oculta: 8 neurônios
        self.fc3 = nn.Linear(8,1)    # Camada de saída: 1 neurônio
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.sigmoid(F.relu(self.fc3(x))) 
        return x

model = ClassBin()
```

**e. Remova todas as camadas de Dropout para uma nova arquitetura.**
*(Não entendi o que isso seria)*
A classe com Dropouts seria:
``` python
class ClassBin(nn.Module):
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 16)  
        self.dropout1 = nn.Dropout(0.2)
        self.fc2 = nn.Linear(16, 8) 
        self.dropout2 = nn.Dropout(0.2) 
        self.fc3 = nn.Linear(8,1)   
        #self.dropout3 = nn.Dropout(0.2) não vejo sentido em dropout aqui
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = self.sigmoid(F.relu(self.fc3(x))) 
        return x

model = ClassBin()
```
O dropout zera algumas ativações de x durante o modo de treino a cada forward e garante que durante o backpropagation esse neurônio não seja afetado, é como se ele não existisse durante aquela iteração; busca garantir que a rede não dependa daquele neurônio específico para predizer.

**f. Treine o novo modelo com os mesmos hiperparâmetros (épocas, taxa de aprendizado, etc.) e compare a acurácia final (de treino e teste) com a do modelo original.**

=> vide notebook 'titanic'

Dois modelos foram treinados com o mesmo dataset do titanic e apresentaram o seguinte resulyado de acurácia:

-------------- MODELO SIMPLES --------------

Acurácia de Treino: 0.7846
Acurácia de Teste: 0.7483

-------------- MODELO REBUSCADO --------------

Acurácia de Treino: 0.8021
Acurácia de Teste: 0.8042

O simples possui a seguinte arquitetura:

```python
class ClassBin(nn.Module):
    # Construtor
    def __init__(self):
        super(ClassBin, self).__init__()
        self.fc1 = nn.Linear(4, 20) # primeira hidden layer
        self.fc2 = nn.Linear(20, 1) # segunda hidden layer
        self.sigmoid = nn.Sigmoid() # output layer com ativação Sigmoid

    # Propagação (Feed Forward)
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

modelo_simples = ClassBin()
```

e o outro:
```python 
class ClassBin2(nn.Module):
    def __init__(self):
        super(ClassBin2, self).__init__()
        self.fc1 = nn.Linear(4, 16)  
        self.dropout1 = nn.Dropout(0.2)
        self.fc2 = nn.Linear(16, 8) 
        self.dropout2 = nn.Dropout(0.2) 
        self.fc3 = nn.Linear(8,1)   
        self.sigmoid = nn.Sigmoid()  

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))
        x = self.dropout2(x)
        x = self.fc3(x)
        x = self.sigmoid(x) 
        return x
    
modelo_rebuscado = ClassBin2()
```
OBS:
- O último modelo possui mais técnicas que o ajudaria a genralizar melhor, como mais camadas ocultas e Dropouts, contudo, dropouts em camadas de poucos neurônios pode acabar ignorando diversos dados importanes e impedindo o aprendizado. Retirar um dos Dropouts e/ou diminuir a taxa para 0.1 melhora os resultados.
- O exemplo no colab do professor usava learning_rate=0.1, mudei para valores menores, como 0.001.

##### 4 -  Usando o modelo original do notebook:

**1. Mude o Otimizador: Substitua o otimizador **Adam** por SGD (Stochastic Gradient Descent). **
**2. Treine o modelo com o SGD.**
=> vide notebook 'SGD'

**3. O que aconteceu com o custo (loss) durante o treinamento? A acurácia final foi melhor ou pior? O SGD com essa taxa de aprendizado pareceu uma boa escolha?**
Usando a taxa de aprendizado sugerida no colab é bem alta, com ela o loss é contante em todas as 100 épocas de treino 
``` 
epoca  0: loss = 0.693
epoca  1: loss = 0.693
epoca  2: loss = 0.693
...
epoca 96: loss = 0.693
epoca 97: loss = 0.693
epoca 98: loss = 0.693
epoca 99: loss = 0.693
``` 
A acurácia final, no modo avaliação, foi melhor: 
```
Acurácia de Treino: 0.593695
Acurácia de Teste: 0.594406
```
Se mudássemos para 0.001 o resultado final continua igual;
Retirando a ReLu que vem logo anes da Sigmoide, e o segundo e terceiro Dropout o resultado melhora para:
```
Acurácia de Treino: 0.697023
Acurácia de Teste: 0.678322
```

