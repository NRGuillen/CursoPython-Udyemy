# MI SOLUCION (ES LITERALEMTE IGUAL QUE LA DE EL PROFESOR)
a = [1,2,4,3,5,6,5,12,67,97,321,43]

numeros_pares = 0
numeros_impares = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

lista_pares = [None] * numeros_pares
lista_impares = [None] * numeros_impares
posicion_pares = 0
posicion_impares = 0

for i in range(len(a)):
    if a[i] % 2 == 0:
        lista_pares[posicion_pares] = a[i]
        posicion_pares += 1
    else:
        lista_impares[posicion_impares] = a[i]
        posicion_impares += 1

print(lista_pares)
print(lista_impares)

# SOLUCION OPTIMIZADA

a = [1,2,4,3,5,6,5]
lista_pares = []
lista_impares = []

for i in range(len(a)):
    if a[i] % 2 == 0:
        lista_pares.append(a[i])
    else:
        lista_impares.append(a[i])

print('========')
print(lista_pares)
print(lista_impares)

# SOLUCION MAS OPTIMIZADA
a = [1,2,4,3,5,6,5]
lista_pares = [num for num in a if num % 2 == 0] # El num del inicio es lo que se guarda en la nueva lista cuando la
# Condición se cumple. En este caso el número del for
lista_impares = [num for num in a if num % 2 != 0]
print('========')
print(lista_pares)
print(lista_impares)