empleados = ['Ruben', 'Alberto', 'Maria']
contrasenas = ['12345', '54321', '32415']

empleado = input('Introduce tu nombre de identificacion: ')
password = input('Introduce tu contraseña de usuario: ')

encontrado = False

for i in range (len(empleados)):
    encontrado = True if empleados[i] == empleado and contrasenas[i] == password else False
    if encontrado:
        break

print(f'Bienvenido {empleado}' if encontrado else 'Empleado no encontrado')
