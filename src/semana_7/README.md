Respostas para exercícios da semana 7 do Onboarding da LIPAI
UFU - Agosto, 2025

Usando [colab](https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/main/notebooks/Aula_18_b_Redes_Neurais_com_PyTorch.ipynb#scrollTo=cPGWImC2wKMo) do Profs. Storopoli & Souza como referência

#  Redes Neurais Artificiais e PyTorch

##### 1 - Com base no material apresentado no notebook, o que é uma função de ativação (como a ReLU)? Por que normalmente usamos entre as camadas?
Funções de ativação ocorrem em cada neurônio após cada cálculo da sua soma ponderada (produto escalar entre entradas e pesos mais bias), isso ocorre para que haja quebra da linearidade, sem ela, mesmo que várias camdas fossem empilhadas seriam equivalentes a uma única camada linear.  
Essa funções permitem que contornor mais precisos possam ser traçados entre as features de modo a determinar melhor a classificação do modelo, sem essa técnica, apenas relações lineares, como E-lógicos e OU-lógicos poderiam ser realizados, para relações mais complexas como XOR é necessário modelos que apliquem ativações em suas camadas internas.

##### 2 -  Explique o que cada uma das seguintes linhas de código faz e por que ela é necessária:
**1. model.train()**
model.train() prepara o modelo para treinamento, isto é, permitir que o pesos e bias dos neurônios adaptáveis sejam atualizados pelo backpropagation, além disso, camadas como nn.Dropout e nn.BatchNorm passam a operar de modo especial. 
*nn.Dropout(p=0.2)* é um objeto utilizado pelo modelo para zerar valores de seus nós internos, cada um tem p chance de ser zerado. Isso ocorre para que o modelo não fique dependente de todos os seus neurônios para a predição, forçandos todos a funcionarem bem juntos. Reduzindo, também, o risco de overfiting. No modo de treinamento o modelo o utiliza a cada forward. 
*nn.BatchNorm(n)* é outro objeto, serve para normalizar saídas internas das camadas durante o forward, garante maior velocidade de treinamento e permite maior learning_rate. 'n' é o númeor de features que será interpretada como uma unidade na normalização, em tabelas n=1, em imagens de 3 canais n=3, se tratar-se de uma sída de convolução com mapas de tamanho 32, n=32. No modo treinamento a normalização depende dos valores de seu batch, se em avaliação média e desvio global são considerados já que normalmente, nesses casos, os batchs são pequenos demais e sua média e desvio poderiam ser pouco representativos. 

**2. optimizer.step()**
- `optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)`
optimizer é um objeto com uma política de avaliação específica, nesse caso Adam. `model.parameters()` é os parâmetros do modelo e `lr` é a taxa com que o modelo aprende, quanto maior mais rápido os parametros mudam.
- `loss.backward()` analisa o grafo gerado pelo forward e retorna os valores novos para os parametros na direção de minimizar a função de custo, isto é, contra a dereivada da função.
- optimizer.step() analisa cada gradiente de cada neurônio e atualiza os valores do tensor utilizando a regra escolhida, por exemplo, se for SGD: param.data -= lr_rate * param.grad.
O que ele faz é dar uma passo extra na direção que minimiza o custo da rede. A cada forward, há um backpropagation e um step, com várias iterações a tendência é alcançar um ótimo local no função de perda.


**3. Qual a diferença fundamental entre os modos model.train() e model.eval()?**