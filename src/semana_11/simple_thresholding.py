import numpy as np
import os
import glob
import cv2

origem = 'Original_ROI_images'
destino = 'results/simple_thresholding'
padrao = os.path.join(origem, '**', '*.tif').replace('\\', '/')
images = glob.glob(padrao, recursive=True)


for path_leitura in images:

    image = cv2.imread(path_leitura)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    (_, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)

    caminho_relativo = os.path.relpath(path_leitura, origem)
    caminho_relativo = os.path.splitext(caminho_relativo)[0] + '.png'
    path_escrita = os.path.join(destino, caminho_relativo)

    os.makedirs(os.path.dirname(path_escrita), exist_ok=True)

    cv2.imwrite(path_escrita, thresh)
