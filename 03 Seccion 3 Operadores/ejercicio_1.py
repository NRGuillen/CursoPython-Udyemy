num1 = int(input('Introduce un numero entero: '))
num2 = int(input('Introduce un numero entero: '))

if num1 >= num2:
    print(f'{num1} > {num2}')
else:
    print(f'{num2} > {num1}')

# Operador ternario
print(f'{num1} > {num2}' if num1 >= num2 else f'{num2} > {num1}')


