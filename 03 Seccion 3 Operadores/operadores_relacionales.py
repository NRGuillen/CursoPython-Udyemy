x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y) # False
print(x is z) # True
print(z is y) # False
print(z is x) # True

print(z is not y) # True

class Factura:
    name : str
    def __eq__(self, value, /):
        return True


a = Factura()
a.name = 'comparas oficina'
b = Factura()
b.name = 'comparas oficin'

print(a is b) # False, no hay 2 objetos iguales, aunque tengan mismos valores, a no se que se igualen directamente
print(a is not b) # True

c = b
print(c is b) # True

print(a == b) # True porque el operador == llama automáticamente a Factura.__eq__(a, b),y ese método devuelve True
print(a.name == b.name) # False

i = 'Hola'
j = 'Hola'

print(i is j) # True, pq los string funcionan distintos, al haber 2 variables con el mismo nombre, python lo detecta y
              # para j, coge el valor de i, si tiene otro valor seria False
print(i == j) # True

k = 20
m = 20

print(k is m) # True Lo mismo que en el string
print(k == m) # True


