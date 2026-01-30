
def main():

    name = input('Introduce tu nombre: ')
    print(f'Hola {name}')

    try:
        numero = int(input('Introduce el numero entero: '))
        print(f'Numero entero {numero}')
    except ValueError:
        print('Introduce el numero decimal correctamente ')

    numero_float = float(input('Introduce el numero decimal: '))
    print(f'Numero decimal {numero_float}')

    return True

valido = False
while valido != True:
    try:
        valido = main()
    except ValueError:
        print('Error: debes introducir bien los datos')

