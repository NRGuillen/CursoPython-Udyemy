# Upper & Lower case
name = 'Ruben Guillen Rojas'
course = 'Curso de Python'
name_upper = name.upper()
print(name.upper()) # Mayusculas todo el str
print(course.lower()) # Minusculas todo el str
print(name_upper == name) # False, porque modifica una copia no el valor real de la variable

# Capitalize & Title
words = 'curso de python'
print(words.capitalize()) # Primera letra en mayuscula y de nuevo inmutable, crea una copia no modifica el original
print(words.title()) # Todas las primeras letras de todo el string en mayuscula

# Remover espacios en blanco en la izquierda o derecha
words = '             hola ruben.                  '
print(words.strip()) # Remueve espacios de la derecha e izquierda
print(words.lstrip()) # Remueve espacios de la izquierda
print(words.rstrip()) # Remueve espacios de la derecha

# Remplazo de palabras en un string
text = ' Hola Java'
print(text.replace('Java', 'Python'))

# Dividir textos por caracteres
text = 'Ruben Guillen ,Python ,Java '
print(text.split(',')[0])
print(text.split(',')[1])
print(text.split(',')[2])

lista = text.split(',')
print(lista)
print(lista[0])
print(lista[1])
print(lista[2] +'\n\nBucle for')

for item in lista:
    print(item)

# De array a string
data = ['Ruben Guillen2', 'Python2', 'Java2']
text = '/'.join(data) # Entre '' puedo poner lo que yo quiera para separar los contenidos del array
print(text)

# Encontrar texto dentro de cadenas de string
text = 'Hola, Ruben que tal estas'
print(text.find('Ruben')) # Devuelve el numero de la posicion del primer char, en este caso 6, si no encuenta retorna -1
print(text.find('Rubennnn'))
print(text.index('tal')) # Devuelve el numero de la posicion del primer char, en este caso 6, si no encuenta retorna una
                         # traza de error, es la unica diferencia con el find
#print(text.index('taaal'))

# Verificar si el string empieza o temrina con una palabra en especifico
text = 'Hola, Ruben que tal estas'
print(text.startswith('Ruben')) # False
print(text.startswith('Hola')) # True

print(text.endswith('Ruben')) # False
print(text.endswith('estas')) # True

# Verifica el tipo de caracteres, para verificar que contenga x caracteres

number = '1234'
decimal = '1234.45'
text = 'Python'
mix = 'Python333'

print(number.isnumeric()) # True
print(decimal.isdecimal()) # False, porque isdecimal comprueba que sea un numero real, no un numero decimal, es decir al
# tener una coma es un numero que no existe, en vez de comprobar si es entero o decimal simplemente comprueba que sea un
# numero
print(text.isalpha()) # True
print(text.isalnum()) # True
print(mix.isalpha()) # False
print(mix.isalnum()) # True

text = '       hola Andres como estas, bienvenido al curso de Python!    '
text_clean = text.strip().capitalize().title()
print(text_clean)

new_text = text_clean.replace('Curso De Python', 'Curso De Python3')
print(new_text)

words = new_text.split(',')
print(words)
print(words[0])
print(words[1])








