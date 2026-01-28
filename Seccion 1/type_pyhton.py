
age0 : int = 40 # asignación con anotación
age1 = 40 # asignación sin anotación

name0 = 'Ruben'
name1 : str = 'Ruben'

print(name0 + ' tiene ' + str(age0) + ' años') # Como concatenamos string con int, hay que parsearlo para que se vea
print(f'{name0} tiene {age0} años') # O podemos utilizar esta forma sin parsear

number_str = '30'
number = int(number_str)
print(f'\nResta: {number - 50}') # Daria error sin el parse
print(f'Suma: {number + 50}')
print(f'Multiplicacion: {number * 50}')
print(f'Division: {number / 50}')

#Admite reasignaciones
x = 10
print(f'\n{x}')
x = 'Hola que tal'
print(x)
