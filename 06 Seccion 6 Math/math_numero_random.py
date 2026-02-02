import random
from math import floor

print(f'Numero aleatorio {random.random() * 10}') # Random de 0 a 9

colores = ['Rojo', 'Amarilo', 'Verde', 'Azul', 'Rosa']

print(f'El color aleatorio elegido es el: {colores[floor(random.random() * 5)]}')

# RANDOM QUE SOLO RETORNA INT
random_int = random.randint(15, 25) # Numero random de 15 a 25
print(random_int)

random_val = random.randint(0, len(colores))
print(random_val)

random_rango = random.randrange(25) # De 0 hasta 24
print(random_rango)

# RANDOM PARA TENER MAS PRECISION EN CALCULOS
random_decimales =  random.uniform(15,25)
print(random_decimales) # 22.303195816311582
