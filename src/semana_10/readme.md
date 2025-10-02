## Semana 10 - Transfer learning: o que é e como usar essa técnica?

2. **Leia o capítulo 8 do livro Introduction to Transfer Learning  Algorithms and Practice:**

[Introduction to Transfer Learning  Algorithms and Practice-chapter-8.pdf](attachment:1e5506fb-e4bb-4ca8-bf16-6246a8fd5915:Introduction_to_Transfer_Learning__Algorithms_and_Practice-chapter-8.pdf)

**Durante a leitura traga anotações curtas de cada item:**

**8.1 Transferability — camadas baixas = traços gerais; camadas altas = traços específicos (estudo clássico tipo Yosinski et al.).**
A trandferência de até as 3 primeiras camadas de uma rede A para uma rede B costuma ser vantajoso por trazer habilidade reconhecimento de regiões genéricas para a rede B. A partir dessas camadas de A o reconhecimento passa a ser de áreas específicas que não ajudam B no seu trabalho.

**8.2 Pré-treino e Fine-tuning — definição formal; quando congelar vs. ajustar.**
A vantagem do fine-tunning é aproveitar de uma rede pre-pretreinada e apenas ajustar para o problema com o qual se lida.

**8.3 Regularização no fine-tuning — L2, L2-SP, EWC/Fisher, DELTA (mapas de feature), BSS, co-tuning.**
O que estamos buscando é formas de diminuir o afatamento da nova rede treinada da rede que já sabe relizar um bom trabalho com outro dataset.
- L2: Weight Decay: penaliza pesos grandes que apareçam durante o treinamento
- L2-SP: Starting Point: em vez de penalizar pesos grandes penaliza o aparecimento de pesos muito distantes dos originais, força a solução à ficar próxima da inicial.
- EWC / Fisher: Usa matriz de Fisher para medir quais pesos eram mais importentes na terefa original. Pesa a regularização de cada parâmetro com essa importância.
- Delta: regulariza os mapas de ativação, não os pesos
- BSS: evita overfitting controlando os autovalores das ativações

**8.4 Uso como extrator de features — pipeline “deep features + SVM/ML clássico”.**
O novo modelo é treinado com features extraídas da rede pré-treinada. O fluxo é Imagem -> passa pela rede pré-treinada até camada x -> vetor de features para o classificador novo -> predição. Isso ocorre tanto no treinamento quando na predição.

**8.5 O que/onde transferir — abrir a caixa-preta: quantas camadas, para quais blocos (ideias de meta-learning).**
Congelar os blocos iniciais é bom pois já aprenderam a idetificar características gerais, os blocos finais utilizam essas informações para predizer, esses rpecisam ser reajustados a cada dataset.

**8.6 Prática em PyTorch — função de fine-tuning e extração de features.**

**8.7 Sumário — quando pré-treinar ajuda mais (datasets pequenos, robustez, OOD, etc.).**
- Datasets pequenos: evita começar o treino do zero com poucos dados
- Robistez: modelos pré-treinados já aprenderam invarâncias úteis
- OOD: ajuda quando os dados são diferentes mas ainda são correlacionados
- velocidade: convergem muito mais rápido
- Baseline forte: em visão, sempre melhor começar com um modelo pré-treinado.   

## Prática

**1 -  Treine do zero (from scratch) o modelo resnet18 já implementado pela biblioteca torchvision (https://docs.pytorch.org/vision/main/models/resnet.html) ao invés do modelo customizado ConvNet proposto na semana 9. Verifique se é necessário alterar o número de classes na camada final para se adequar ao dataset MNIST. Mantenha os mesmos hiperparâmetros da semana 9. Compare os resultados:**

No notebook ex1_resnet18_from_scrtch

**2 -  Utilize o modelo resnet18 com os pesos pré-treinados do imagenet (ResNet18_Weights.IMAGENET1K_V1) para avaliar os datasets ImageNet e MNIST. Você não deve treinar o modelo, apenas rodar a etapa de testes com o modelo em modo de avaliação. Não executar as fases de treinamento e validação.  Quais foram os resultados? O que você esperava antes de rodar os experimentos? Explique os resultados.**

No notebook ex2_restnet18_mnist_imgnet

**3 -  Utilize o modelo resnet18 com os pesos pré-treinados do ImageNet  para avaliar o dataset MNIST. Dessa vez você deve treinar e avaliar o modelo de 3 formas:**

**3.1 - Congele todas as camadas (Layer 1, 2, 3 e 4) e treine apenas a última camada (fc).**
O treino levou alguns muitos minutos, exercício no notebook ex3-1_treino_mnist

**3.2 - Fine tuning parcial “descongelando” apenas o último bloco da rede resnet18 (Layer 4) e última camada (fc)**
O treino levou uma hora, execício no notebook ex3-2_treino_mnist

**3.3 - Fine tuning total “descongelando” todos os blocos da rede resnet18 (Layer 1-4) e última camada (fc)**
O treino levou duas horas, execício no notebook ex3-3_treino_mnist


**4 - Compare os resultados no dataset MNIST usando as métricas de acurácia e f1-score no conjunto de teste:**

1. Treinamento do zero (Ex 1)
2. Somente a camada fc (Ex. 3.1)
3. Fine tuning parcial (Ex. 3.2)
4. Fine tuning total (Ex. 3.3)

Quanto mais se teina as camadas melhor é o resultado do modelo; sem treinamento o resultado é muito ruim; omodelo apenas chuta suas predições, obteve acurácia de 8%, quando treinamos apenas a última camada, fc, o resultado subiu para 96% de acurácia.
Outra coisa a se levar emconta é o tempo de treinamento: o treino de apenas a última cadama levou alguns minutos, treinar a camada 4 e a fc levou 1h, treinar toda a rede levou muito mais. Num treinamento futuro é importante levarmos em conta o peso de aumentar um pouco mais a acurácia e o custo de treinamento.
