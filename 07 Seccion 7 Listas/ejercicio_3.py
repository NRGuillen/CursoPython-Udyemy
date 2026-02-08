"""Leer 7 números por teclado para llenar una lista y a continuación calcular el promedio de los números positivos, el
promedio de los negativos y contar el número de ceros."""

numeros_positivos = 0
numeros_negativos = 0
numeros_ceros = 0

for i in range(7):
    numero =  float(input(f'Introduce el Numero[{i+1}]: '))
    if numero > 0:
        numeros_positivos += 7
    elif numero < 0:
        numeros_negativos += 7
    else:
        numeros_ceros += 7

promedio_numeros_positivos = numeros_positivos // 7
promedio_numeros_negativos = numeros_negativos // 7
promedio_numeros_ceros = numeros_ceros // 7

print(f'Promedio numeros positivos: {promedio_numeros_positivos}'
      f' | Promedio numeros negativos: {promedio_numeros_negativos}'
      f' | Promedio numeros ceros: {promedio_numeros_ceros}')