for i in range(5):
    print(i)

print('===========')

for i in range(0, 10, 2): # Empieza desde 0 hasta 2 y se incrementa de 2 en 2
    print(i)

print('===========')

for i in range(10, 0, -1): # Empieza desde 10 hasta 0 y va restando -1
    print(i)

print('===========')

for i in range(10, -1, -1): # Empieza desde 10 hasta -1 y va restando -1
    print(i)

print('===========')

nombres = ['Ruben', 'Andres', 'Lucia', 'Alberto']
for nombre in nombres: # Posicion por posicion
    print(nombre)

for nombre in nombres[0]: # Posicion especifica, lo coge char por char
    print(nombre)

for nombre in nombres: # Itera 4 veces los nombres caracter por caracter
    print('====')
    for nombres_por_char in nombre:
        print(nombres_por_char)

print('===========')

email = 'andres.correo@hotmail.com'
for c in email: # Char por char
    print(c)

print('===========')



