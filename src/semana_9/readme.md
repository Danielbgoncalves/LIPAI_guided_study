# SEMANA 9: Data augmentation: o que é e como usar essa técnica?

**1 - Modifique a etapa de transformações (trans) para incluir uma rotação aleatória nas imagens de treinamento. Utilize torchvision.transforms.RandomRotation com um ângulo de até 15 graus. Como ficaria a nova definição de transforms.Compose?**
```python
    trans = transforms.Compose([
        torchvision.transforms.RandomRotation(15),
        transforms.ToTensor(), 
        transforms.Normalize((0.1307,), (0.3081,))
    ])
```
Agora a cada `___getitem__` dos data sets a imagem retornada pode ser diferente pois há fator aleatório de rotação, antes o retorno era determinístico.

---

**2 - Construa uma nova estratégia de transformação chamada trans_aumentado que aplique sequencialmente as seguintes técnicas de aumento de dados:**

- Translação horizontal e vertical aleatória de até 10% da dimensão da imagem (RandomAffine).
- Zoom aleatório, variando a escala da imagem entre 90% e 110% (RandomAffine).
- Alteração de perspectiva (RandomPerspective).

**Após criar essa estratégia, substitua a etapa de transformação original no train_dataset e treine o modelo novamente.**

```python
trans_aumentado = transforms.Compose([
      torchvision.transforms.RandomRotation(15),
      torchvision.RandomAffine(
          degres=10, 
          translate=(0.1,0.1),          # translação (horizontal, vertical)
          scale=(0.9, 1.1)              # zoom (mínimo, máximo)
      ), 
      transforms.RandomPerspective(
          distortion_scale=0.5,         # intensidade
          p=0.3,                        # probabilidade
          interpolation=3
      ),
      transforms.ToTensor(), 
      transforms.Normalize((0.1307,), (0.3081,))
    ])
```

---

**3 - A transformação transforms.RandomHorizontalFlip() é muito comum em problemas de visão computacional. Você a aplicaria para o dataset MNIST? Justifique sua resposta pensando em como essa transformação afetaria a classificação de dígitos específicos (por exemplo, o '6' e o '9').**
Em identificaçõ de objetos ou animais, os elementos de ponta cabeça ainda são os mesmo elementos e é vantajoso que o modelo treine com essas variações, contudo, um seis invertido passa a ser outro número, o nove. Deste modo, o treino ocorreria com rotulagens que enganariam o aprendixado do modelo. 

**4 - Crie 2 pipelines de treinamento distintas:**

- Baseline: O modelo original, sem aumento de dados explícito (além da normalização).
- Básico: Usando RandomAffine (rotação, translação).
- Avançado: Usando TrivialAugmentWide combinado com RandomErasing.
- Mixup/CutMix: Implemente uma das técnicas de mistura no loop de treinamento.

Treine com o modelo da rede CNN com os pipelines escolhidos. Mantenha todos os outros hiperparâmetros (taxa de aprendizado, número de épocas, otimizador) constantes e compare os resultados:

- Acurácia final no conjunto de teste.
- Velocidade de convergência (observe as curvas de custo).

A acurácia caiu mais rapidamente e fixou-se mais perto do 0 durante os treinos com pipelines baseline e básica, no treino com pipeline ela variou bem mais por volta do 0.5
Contudo durante a avaliação com imagens inéditas o modelo com pipeline avançada teve acurácia 86.96 enquanto os outros ficaram com 67 e tantos.