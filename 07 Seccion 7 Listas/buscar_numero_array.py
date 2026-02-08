numeros = [1,5,3,2,5,7,8,9,3,1,234,243]

numero_buscar = int(input('Introduce el numero a buscar: '))

numero_encontrado = False
posicion = 0
for i in numeros:
    if numero_buscar == i:
        numero_encontrado = True
        posicion = i
        break

print(f'Numero encontrado en la posicion {posicion}' if numero_encontrado == True else 'Numero no encontrado')

############################################################################################################

nombres = ['Ruben', 'Alberto', 'Maria']
posicion = -1

nombre_buscar = input('Introduce el nombre a buscar: ')

for i in range(len(nombres)):
    if nombre_buscar.lower().__eq__(nombres[i].lower()):
        posicion = i
        break

print(f'Nombre encontrado en la posicion {posicion + 1}' if posicion >= 0 else 'Nombre no encontrado')

# SISTEMA OPTIMIZADO

nombres = ['Ruben', 'Alberto', 'Maria']
nombre_buscar = input('Introduce el nombre a buscar: ')

resultado = next(((i, nombre) for i, nombre in enumerate(nombres) if nombre.lower() == nombre_buscar.lower()), (-1, None))
# next sirve para que tras encontrar el primer valor se pare, no es necesario
# enumerate nos da el indice del array nombre
# i -> indice
# nombre -> valor de la posicion
# Si no encuentra el nombre retorna un -1 y un None, de lo contrario retorna la posicion de i y el nombre
posicion, encontrado = resultado

print(f'Nombre {encontrado} encontrado en la posicion {posicion+1}' if posicion >= 0 else 'Nombre no encontrado')