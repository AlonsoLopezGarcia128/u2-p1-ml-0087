import numpy as np

print("---- LLenar matriz de cero ----")
matriz = np.zeros([3,5]) # 3 filas x 5 columnas
print(matriz)
print(" ")

print("---- LLenar matriz de unos ----")
matriz = np.ones([3,5]) # 3 filas x 5 columnas
print(matriz)
print(" ")

print("---- LLenar matriz vacio ----")
matriz = np.empty([3,5]) # 3 filas x 5 columnas
print(matriz)
print(" ")

print("---- LLenar lista con rango ----")
# El primer parametro es el valor inicial
# El segundo parametro es el valor final
# El tercer parametro es el incremento
matriz = np.arange(0, 10, 2) 
print(matriz)
print(" ")

print("---- LLenar lista con rango No 2----")
matriz = np.arange(0, 10, 1) 
print(matriz)