"""Escriba un programa que imprima el número más alto de un arreglo de 7 elementos (de rango 11 a 99), por ejemplo {14,
33, 15, 36, 78, 21, 43}, si se repite un valor considerar uno solo."""

# OPCION 1
numeros =  [14, 33, 15, 36, 78, 21, 43]
num_max = 0

for i in range(len(numeros)):
    if numeros[i] > num_max:
        num_max = numeros[i]
print(num_max)

# OPCION 2
print(max(numeros))

# OPCION 3
num_max = numeros[0]
for i in numeros:
    if i > num_max:
        num_max = i
print(num_max)

# SOLUCION PROFESOR

arreglo = [14, 33, 15, 36, 78, 21, 43, 0, 0, 0]
maximo = 0

for i in range(7):
    maximo = maximo if maximo > arreglo[i] else arreglo[i]

print("El valor más alto es:", maximo)