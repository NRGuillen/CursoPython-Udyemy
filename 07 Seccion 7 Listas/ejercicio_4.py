"""Para la tarea se debe crear una lista con 10 elementos (enteros en el rango de 1 a 9). Escriba un programa que
imprima el número que tiene más ocurrencias en la lista y también imprimir la cantidad de veces que aparece en el
arreglo.

Por ejemplo, para el arreglo: {1, 2, 3, 3, 4, 5, 5, 5, 6, 7}

Como resultado debería imprimir lo siguiente:

La mayor ocurrencias es: 3 El elemento que más se repite es: 5
En el ejemplo, el elemento que más se repite en el arreglo es el número 5 con una ocurrencia de 3 veces."""

numeros = [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8]

num_mas_repetido = 0
ultimo_veces_repeticas = 0

for i in range(len(numeros)):
    veces_repetidas = 0
    for j in range(len(numeros)):
        if numeros[i] == numeros[j]:
            veces_repetidas += 1

        if veces_repetidas >= ultimo_veces_repeticas:
             num_mas_repetido = numeros[i]
             ultimo_veces_repeticas = veces_repetidas

print(f'El elemento que más se repite en el arreglo es el número {num_mas_repetido} con una ocurrencia '
      f'de {ultimo_veces_repeticas} veces.')


