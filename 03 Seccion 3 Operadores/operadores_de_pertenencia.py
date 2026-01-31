nombres = ['Ruben', 'Maria', 'Josefa', 'Pepe']

resultados = 'Andres' in nombres
print(resultados) # Falso porque andres no existe en el array
resultados = 'Ruben' in nombres
print(resultados) # True, sensible a mayusculas/minusculas
resultados = 'Mario' not in nombres
print(resultados) # True

print('Carlos' in 'Hola carlos como te va!') # Falso, porque carlos está en minusculas
print('te' in 'Hola Carlos como te va!') # True
print('H' in 'Hola carlos como te va!') # True
print('h' not in 'Hola carlos como te va!') # True, porque no hay h minuscula
