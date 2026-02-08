productos = ['Hola que tal', 'Buenas que tal', 'Si hola que tal', 'No que tal', 'JAJA que tal' ,'Pues que tal', 'SII']

for i in range(len(productos)): # Con doble '//' es una division entera
    for j in range(len(productos) - i - 1):
        if productos[j + 1] < productos[j]: # Compara el valor j, con el siguiente valor de la lista j + 1
            productos[j] , productos[j + 1] = productos[j + 1] , productos[j] # Al vuelo

for i in productos:
    print(i)
    