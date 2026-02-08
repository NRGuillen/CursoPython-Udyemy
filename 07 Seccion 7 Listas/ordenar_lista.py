productos = [None] * 7
productos [0] = 'Hola que tal'
productos [1] = 'Buenas que tal'
productos [2] = 'Si hola que tal'
productos [3] = 'No que tal'
productos [4] = 'JAJA que tal'
productos [5] = 'Pues que tal'
productos [6] = 'Hombre que tal'

for i in productos:
    print(i)

# ORDENA LA LISTA
productos.sort()
# Orden de forma alfabetica A > Z
print('================')
for i in productos:
    print(i)

# Orden de forma alfabetica Z > A
print('================')
for i in reversed(productos):
    print(i)

# Orden de forma alfabetica Z > A
print('================')
for i in productos[::-1]:
    print(i)

numeros = [None] * 5
numeros[0] = 10
numeros[1] = 51
numeros[2] = 31
numeros[3] = 41
numeros[4] = 891

print('================')
numeros.sort()
for i in numeros:
    print(i)
