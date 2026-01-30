"""Crear una archivo py donde el desafío es buscar el número menor de mínimo 10 valores enteros, ingresar la cantidad
de números a comparar, luego utilizando una sentencia for iterar el numero de veces (ingresado) para pedir el numero
entero, entonces se requiere:

Calcular el menor número e imprimir el valor.

¡Si el menor número es menor que 10, imprimir "El número menor es menor que 10!". si no, imprimir " el numero menor es
igual o mayor que 10!"."""

numeros = [12, 32, 43, 23, 34, 67, 11, 32, 56, 76]
numero_menor = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

for numero in numeros:
    if numero < numero_menor:
        numero_menor = numero

print(f'El numero menor es: {numero_menor}')

if numero_menor >= 10:
    print("El numero menor es igual o mayor que 10!")
else:
    print("El número menor es menor que 10!")
