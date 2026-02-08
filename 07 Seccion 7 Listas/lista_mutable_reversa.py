# MI MANERA DE DAR VUELTA A LA LISTA SIN METODOS
productos = ['Hola que tal', 'Buenas que tal', 'Si hola que tal', 'No que tal', 'JAJA que tal' ,'Pues que tal', 'SIII']
vueltas = 0
producto_cambio = [None] * len(productos)
for i in productos:
    producto_cambio[vueltas] = productos[len(productos) - vueltas - 1]
    vueltas += 1

productos = producto_cambio

for i in productos:
    print(i)

# MANERA DEL PROFESOR DEL CURSO
print('==============')
productos = ['Hola que tal', 'Buenas que tal', 'Si hola que tal', 'No que tal', 'JAJA que tal' ,'Pues que tal', 'SIII']
for i in range(len(productos) // 2): # Con doble '//' es una division entera
    current = productos[i]
    reverse = productos[len(productos) - 1 - i]
    productos[i] = reverse
    productos[len(productos) - 1 - i] = current

for i in productos:
    print(i)
