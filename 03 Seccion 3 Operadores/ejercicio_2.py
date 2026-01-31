"""Suponiendo un estanque de gasolina (gas) con capacidad 70 litros, se requiere un programa que pida la medida actual
en litros y mostrar el resultado de la forma: Insuficiente, Suficiente, Medio...

La medida o capacidad actual del estanque puede ser en tipo float, para una mejor precisión, pero también puede ser del tipo int.

Si la capacidad actual es 70 litros: imprimir Estanque lleno
Si está entre 60 y menor a 70: imprimir Estanque casi lleno
Si está entre 40 y menor a 60: imprimir Estanque 3/4
Si está entre 35 y menor a 40: imprimir Medio Estanque
Si está entre 20 y menor a 35: imprimir Suficiente
Si está entre 1 y menor a 20: imprimir Insuficiente"""

combustible = float(input('Introduce la cantidad actual de combustible en el tanque: ' ))

comprobacion = True

if combustible > 70:
    print('Has introducido una cantidad mayor al almacenamiento del tanque')
    comprobacion = False

if comprobacion:
    if combustible == 70:
        print('Estanque lleno')
    elif 60 <= combustible < 70:
        print('Estanque casi lleno')
    elif 40 <= combustible < 60:
        print('Estanque 3/4')
    elif 35 <= combustible < 40:
        print('Medio Estanque')
    elif 20 <= combustible < 35:
        print('Suficiente')
    elif 1 <= combustible < 20:
        print('Insuficiente')

