productos = ['Hola que tal', 'Buenas que tal', 'Si hola que tal', 'No que tal', 'JAJA que tal' ,'Pues que tal', 'AA']

for i in range(len(productos)): # Con doble '//' es una division entera
    for j in range(len(productos)):
        if productos[i] < productos[j]:
            volatil = productos[i]
            productos[i] = productos[j]
            productos[j] = volatil

for i in productos:
    print(i)
