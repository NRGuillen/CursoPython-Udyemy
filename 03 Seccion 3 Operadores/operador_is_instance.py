num = 10
text = 'Crenaod un objeto de la clase str'
num_decimal = 3.1231

b1 = isinstance(text, str) # Primero el nombre de la variabl y luego su tipo
print(f'Text es de tipo str =  {b1}') # True

b2 = isinstance(num, int)
print(f'{num} es de tipo int =  {b2}') # True

b3 = isinstance(num_decimal, float)
print(f'{num_decimal} es de tipo float =  {b3}') # True

b4 = isinstance(num, str)
print(f'{num} es de tipo str =  {b4}') # False

# Como b4 es = a una instancia de num, str retorna un false porque es un numero de tipo int no str, y por ende b4 en
# la siguiente comprobacion vale False y por lo tanto de tipo bool
b5 = isinstance(b4, bool)
print(f'{b4} es de tipo booleano =  {b5}') # True

data = 3.14
b6 = isinstance(data, (int, float)) # Compruebo si el tipo data es int OR float
print(f'{data} es del tipo entero o decimal = {b6}') # True

b7 = isinstance(text, (int, float))
print(f'"{text}" es del tipo entero o decimal = {b7}')

# Objetos
class Persona:
    pass # No hace nada, solo sirve para decir que hay que añadir algo

class Animal:
    pass

class Dog(Animal): # Dog hereda de la clase animal
    pass

dog = Dog()
b7 = isinstance(dog, Dog)
print(f'{dog} es instancia de Dog = {b7}') # True

b8 = isinstance(dog, Animal)
print(f'{dog} es instancia de Dog = {b8}') # True

b9 = isinstance(dog, Persona)
print(f'{dog} es instancia de Dog = {b9}') # False

ruben = Persona()
b10 = isinstance(ruben, Persona)
print(f'{ruben} es instancia de Dog = {b10}') # True

b11 = isinstance(ruben, Animal)
print(f'{ruben} es instancia de Dog = {b11}') # False

b12 = isinstance(ruben, Dog)
print(f'{ruben} es instancia de Dog = {b12}') # False

b13 = isinstance(ruben, (Dog , Persona))
print(f'{ruben} es instancia de Dog = {b13}') # True
