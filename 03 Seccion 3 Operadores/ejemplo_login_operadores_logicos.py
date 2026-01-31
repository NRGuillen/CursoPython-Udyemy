empleados = ['Ruben', 'Alberto', 'Maria']
contrasenas = ['12345', '54321', '32415']

empleado = input('Introduce tu nombre de identificacion: ')
password = input('Introduce tu contraseña de usuario: ')

encontrado = False

for i in range (len(empleados)):
    if empleados[i] == empleado and contrasenas[i] == password:
        print(f'Bienvenido {empleado}')
        encontrado = True
        break

if not encontrado:
    print('Error: identificacion incorrecta')