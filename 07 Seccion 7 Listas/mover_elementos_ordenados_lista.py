numeros =  [14, 33, 15, 36, 78, 21, 43] # OBJETIVO [43, 14, 33, 15, 36, 78, 21]

ultimo = numeros[len(numeros) - 1]

for i in range(len(numeros) -2, -1, -1):
    numeros[i + 1] = numeros[i]

numeros[0] = ultimo

print(numeros)