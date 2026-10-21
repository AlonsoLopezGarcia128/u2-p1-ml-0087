# Alonso Lopez Garcia NC = 0087
import numpy as np

# lista
calificaciones = np.array([60, 70, 90])
print("---------- Ejemplo 1 imprimir calificaciones ----------")
print(calificaciones) # imprime las listas de calificaciones
print(type(calificaciones)) # Muestra el tipo de arreglo

print(" ")
print("---------- Ejemplo 2 | 0 dimensiones de un array ----------")
calificaciones = np.array(60)
print(calificaciones) # Imprime las calificaciones 
print("Dimension : ", calificaciones.ndim) # Imprime las dimensiones de calificaciones 0

print(" ")
print("---------- Ejemplo 3 | 1 dimension de un array----------") 
calificaciones = np.array([60, 70, 90]) # Define lista de calificaciones
print(calificaciones) # Imprime las calificaciones 
print("Dimension : ", calificaciones.ndim) # Imprime las dimensiones de calificaciones 1

print(" ")
print("---------- Ejemplo 4 | 2 dimensiones de un array----------")
calificaciones = np.array([
    [60, 70, 90],
    [50, 80, 98]
    ]) # Un arreglo de dos dimensiones es como una tabla en excel
print(calificaciones) # Imprime las calificaciones 
print("Dimension : ", calificaciones.ndim) # Imprime las dimensiones de calificaciones 1 

print("---------- Ejemplo 5 ----------")

print("Alonso Lopez Garcia NC = 0087")
