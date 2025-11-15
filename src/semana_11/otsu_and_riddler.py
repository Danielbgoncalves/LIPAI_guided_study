import numpy as np
import os
import glob
import cv2
import matplotlib.pyplot as plt
import mahotas
import pandas as pd

def dice_coef(img, ref):
    img_bin = img > 0
    ref_bin = ref > 0

    inters = np.sum(img_bin & ref_bin)
    img_len = np.sum(img_bin)
    ref_len = np.sum(ref_bin)

    if img_len + ref_len == 0:
        return 1.
    
    return (2. * inters) / (img_len + ref_len) 
    
# Lê csv
csv_path = 'segmentacao.csv'
df = pd.read_csv(csv_path)
COLUNA = 'otsu_riddler_threscholding'
linha_atual = 0

# Coleta imagens a serem analisadas
caminho_de_origem = 'Original_ROI_images'
padrao_leitura = os.path.join(caminho_de_origem, '**', '*.tif').replace('\\', '/')
images_leitura = glob.glob(padrao_leitura, recursive=True)

# Coleta imagens de referencia
caminho_origem_ref  = 'Gold_Standard_Semantic_Segmentation'
padrao_ref = os.path.join(caminho_origem_ref, '**', '*.png').replace('\\', '/')
images_ref = glob.glob(padrao_ref, recursive=True)

print("Total imagens:", len(images_leitura), len(images_ref))

for img_leitura_path, img_ref_path in zip(images_leitura, images_ref):

    # Lê imagem original
    img_leitura = cv2.imread(img_leitura_path)
    img_leitura = cv2.cvtColor(img_leitura, cv2.COLOR_BGR2GRAY)

    # Segmentação por threshold
    blurred = cv2.GaussianBlur(img_leitura, (5, 5   ), 0)
    T = mahotas.thresholding.otsu(blurred)
    thresh = img_leitura.copy()
    thresh[thresh > T] = 255
    thresh[thresh < T] = 0
    thresh = cv2.bitwise_not(thresh)

    # Lê imagem de referência
    img_ref = cv2.imread(img_ref_path)
    img_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY)

    # plt.figure(figsize=(8,3))

    # plt.subplot(1, 3, 1)
    # plt.title("Original")
    # plt.imshow(img_leitura, cmap='gray')
    # plt.axis('off')

    # plt.subplot(1, 3, 2)
    # plt.title("Original")
    # plt.imshow(thresh, cmap='gray')
    # plt.axis('off')

    # plt.subplot(1, 3, 3)
    # plt.title("Original")
    # plt.imshow(img_ref, cmap='gray')
    # plt.axis('off')

    # plt.tight_layout()
    # plt.show()

    # Calcula coeficiemte de dice
    dice = dice_coef(thresh, img_ref)

    # adicoina no df
    df.loc[linha_atual, COLUNA] = dice
    linha_atual +=1

mean_col_name = f"{COLUNA}_mean"
df.loc[0, mean_col_name] = df[COLUNA].mean()
df.to_csv(csv_path, index=False)
