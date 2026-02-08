# LISTA DINAMICA
numbers = [0] * 5 # Lista reservada para 5 elementos

numbers[0] = 1
numbers[1] = 2
numbers[2] = 3
numbers[3] = 4
numbers[4] = 'Ruben'

for i in range(len(numbers)):
    print(numbers[i])

# LISTA DINAMICA
# Añadimos contenido a la lista, se rellena de forma ordenada, el primer append en el [0] o en el ultimo que exista
numeros = []
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append('Ruben')

for i in range(len(numeros)):
    print(numeros[i])

# LISTA ESTATICA
numeros = [1, 2, 3, 4, 'Ruben']
for i in range(len(numeros)):
    print(numeros[i])

#FOREACH
for i in numeros:
    print(i)
