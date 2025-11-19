# Sobre a leitura do artigo Fully Convolutional Networks for Semantic Segmentation

1. A principal dos modelos anteriores, de predição de classes, era a não rastreabilidade de o que da imagem produziu o resultad. A análise se dava sobre a imagem por completo; o resultado era um vetor de probabilidades. 
2. A nova ideia é usar as camadas completamente conectadas (FC) como convoluções 1x1. Deste modo toda a rede seria convolucional e faria 'predições densas'.
3. Junta-se as camadas profundas e rasas. Informações globais resolvem o "o que há na imagem", as rasas dizem "onde".
4. As redes CNN de classificação usar FC recebem, ovrigatóriamente, o mesmo tamanho de imagem, se o tamanho mudar é preciso redimensionar suas estruturas e retreina-la, enquanto as convoluções e poolings funcionam igualmente para qualquer entrada.
5. Além disso a FC retira as ideias de posição dos dados quando transforma tudo em vetor. Uma solução é operar ali uma convolução. É possível fazer essa troca mantendo o mesmo sentido no resultado final.
6. Se a FC recebia 7x7x512 e tinha 4096 neurônios, a nova conv.terá kernel 7x7, 512 canais e 4096 filtros.
7. O output após essa conversão será (n=número de covoluções aplicadas): H/2^n x W/2^n x num_classes, isso é muito meor que o input => coarse (algo grosseiro)
8. Uma solução imediata seria fazer output.resize bilinear 2^n vezes mas isso ainda é grosseiro. Melhor é fazer **Convolução Transposta** (ou Deconvolution) que realiza upsample 2^n até a imagem ficar com o tamanho correto. O melhor é que a deconvolution pode ser aprendida no treino.
9. O treino da imagem interira como insight, mais rápido e eficiente que por patches.
10. Parte do problema é que upsample 32x é grosseiro ainda (Considenrando n = 5 o que é comum) pois vem de dados que foram comprimirdos 32x. Uma solução é juntas o resultados desses upsamples com os mapas de ativação intermediários das polls.
11. A poll 4 tem tamanho H/16 x W/16, então é feito upsample 2x na saída da última conv, fundida com essa ativação, depois sofre mais upsamples até o tamanho inicial.
12. Junta-se boa semnatica das camadas profundas e boa localização e camadas rasas
13. Muito mais eficeinte que a técina estado-da-arte da época em que foi desenvolvido (SDS). Também é muito mais rápido.
14. SDS levava 40 segundos por imagem, o FCN leva 150ms. O skip connection (juntar o upsampling com os mapas de ativação dos poll) ajudou a subir as notas no benchmarks.

**end-to-end**: a cada imagem de entrada é gerada uma mascara de saida. Todas as camadas da ede aprendem juntas.

**pixel-to-pixel**: a rede prevê um rótulo para cada pixel. Com o FCN todos os pixels são previstos juntos. FCN foi a primeira a unir essas duas ideias de segmentação.