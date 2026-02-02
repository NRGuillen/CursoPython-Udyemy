text = "Ruben Guillen"
print(text[0:6]) # Desde el char 0 hasta el 6 R u b e n
print(text[0:6:2]) # Desde el char 0 hasta el 6 saltando de 2 en 2 R b n
print(text[6:]) # Desde el 7 hasta el final del string
print(text[:6]) # Desde el inicio hasta el 6
print(text[::]) # Desde el inicio hasta el final y por defecto 1 (Todo)
print(text[::-1]) # Da la vuelta a todo el string y sus palabras, con numero positivo le dices que empiece desde el
                  # inicio y con uno negativo desde el final

text = "Hola mundo"
mew_text = text[:5] + text[5:].replace('mundo', 'Python')
print(mew_text) # Hola Python

text = "Python es genial"
sperarar_por_string = text[:9].split(' ')
print(sperarar_por_string) # ['Python', 'es']

array = text.split(' ')
print(array[:2]) # Hasta la 2 posicion del array 0 | 1 ['Python', 'es']

parts_revese = array[::-1]
print(parts_revese) # ['genial', 'es', 'Python']

text_reverse = ' '.join(parts_revese)
print(text_reverse) # genial es Python

text = "Python"
print(text[:2].lower() + text[2:].upper()) #pyTHON

text = "    Hola Python  "
print(text.strip()[5:]) # Python


