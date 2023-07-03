import cv2
import numpy as np

def filtro_roberts(imagem):
    # Converter a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicar o filtro Roberts
    roberts_x = cv2.filter2D(imagem_cinza, -1, np.array([[1, 0], [0, -1]], dtype=np.float32))
    roberts_y = cv2.filter2D(imagem_cinza, -1, np.array([[0, 1], [-1, 0]], dtype=np.float32))

    # Combinação dos resultados nas direções x e y
    roberts = cv2.addWeighted(roberts_x, 0.5, roberts_y, 0.5, 0)

    return roberts

# Carregar a imagem
imagem = cv2.imread('C:/Users/User/Downloads/Original.jpg')

# Aplicar o filtro Roberts
imagem_filtrada = filtro_roberts(imagem)

# Exibir a imagem original e a imagem filtrada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Filtrada (Roberts)', imagem_filtrada)
cv2.waitKey(0)
cv2.destroyAllWindows()