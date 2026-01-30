number = 5

match number:
    case 1:
        print('El numero es 1')
    case 2:
        print('El numero es 2')
    case 3:
        print('El numero es 3')
    case 4:
        print('El numero es 4')

    case _: # Default
        print('Opcion no valida')

def opcion(number):
    if number == 1:
        return 'Seleccionaste la opcion 1'
    elif number == 2:
        return 'Seleccionaste la opcion 2'
    elif number == 3:
        return 'Seleccionaste la opcion 3'
    elif number == 4:
        return 'Seleccionaste la opcion 4'
    else:
        return 'Opcion no valida'

print(opcion(3))

name = input('Ingresa el nombre de Persona: ')

match name:
    case 'Pepe':
        print('Hola Pepe, que tal')
    case 'Pepe':
        print('Hola Juan, como te va')
    case 'Maria':
        print('Hola Maria, bienvenida')
    case _:
        print('Hola invitado')

match name:
    case 'Pepe' | 'Juan' | 'Maria':
        print('Hola hermanos, que tal')
    case 'Jhon' | 'Josefa':
        print('Hola padres, como te va')
    case 'Andres':
        print('Hola Primo')
    case _:
        print('Hola invitado')