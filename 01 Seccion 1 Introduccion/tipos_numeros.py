from decimal import Decimal, getcontext

age = 30
big_int = 400000000000006876876
decimal = 3.1415

print(age)
print(type(age)) # te dice el tipo de la variable

print(big_int)
print(type(big_int)) #int

print(decimal)
print(type(decimal)) #float

number_complex = 2 + 3j
print(type(number_complex))

# Alta precision de operaciones
getcontext().prec = 10
num1 = Decimal('10.123456789')
num2 = Decimal('2.1')
resultado = num1 + num2
print(resultado)

number = 42
decimal_number = float(number)
integer_number = int(3.1242)
print(decimal_number)
print(integer_number)

