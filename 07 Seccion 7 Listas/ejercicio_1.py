"""Llenar un arreglo de 10 elementos. Luego debemos mostrarlos en el siguiente orden: el último, el primero,
el penúltimo, el segundo, el antepenúltimo, el tercero, y así sucesivamente."""

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros) // 2):
    print(f'{numeros[i]} : {numeros[(len(numeros) - 1) - i]}')