# While
print('========== While')
i = 0
while i < 5:
    print(f'El contador es: {i}')
    i += 1

names = ['Andres', 'Luna', 'Juan', 'Margarita', 'Pedro']
count = 0
print(len(names)) #len(names) = la longitud del array (5)
while count < len(names): # len(names) = la longitud del array
    print(f'Nombres en la posicion {count}: {names[count]}')
    count += 1


print('========== do While')
# do While
i = 0
while True:
    print(i)
    i+= 1
    if i >= 5:
        break


print('========== do While ejemplo practico')

correct_number = 7

while True:
    attemp = input('Adivina el numero: ')
    if int(attemp) == correct_number: # Parseo el attemp porque lo coge como string, o también podemos parsear el attemp del input
        print('Has acertado el numero!')
        break
    else:
        print('Has fallado, intentelo de nuevo:')


