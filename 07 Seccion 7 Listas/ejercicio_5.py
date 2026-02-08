"""Escribir un programa que recorra una lista y genere un histograma en base a los valores de este.

La lista debe contener 12 elementos que corresponden a números enteros de rango 1 al 6.

Un histograma es una representación gráfica (de puntos o barra) de que tanto un elemento aparece en un conjunto
de datos, es decir debe mostrar la frecuencia para todos los números del 1 al 6, incluso si no están presente en
el arreglo.

Por ejemplo para el arreglo {4, 3, 4, 6, 6, 4, 1, 4, 5, 4, 1, 1} el histograma debería ser:

1: ***
2:
3: *
4: *****
5: *
6: **
Para la tarea usaremos el asterisco(*) como representación gráfica para el histograma."""

numeros = [4, 3, 4, 6, 6, 4, 1, 4, 5, 4, 1, 1]
vistos = []

for i in range(len(numeros)):
    if numeros[i] not in vistos:
        vistos.append(numeros[i])
        suma = 0
        for j in range(len(numeros)):
            if numeros[i] == numeros[j]:
                suma += 1
        print(f"{numeros[i]}: {'*' * suma}")

