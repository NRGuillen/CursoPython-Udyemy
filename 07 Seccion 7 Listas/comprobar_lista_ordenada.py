# MI SOLUCION, SOLO DETECTA SI ESTA O NO ORDENADA
a = [1,2,3,4,5,6]

num_anterior = a[0]
lista_ordenada = True
for i in range(len(a)):
    if a[i] < num_anterior:
        lista_ordenada = False
    num_anterior = a[i]
print('La lista no esta ordenada' if lista_ordenada == False else 'La lista esta ordenada')

# SOLUCION DEL PROFESOR, DETECTA COMO ESTÁ ORDENADA O SI ESTÁ ORDENADA
a = [1,2,4,3,5,6]
is_asc = False
is_desc = False

for i in range(len(a) - 1):
    if a[i] > a[i+1]:
        is_desc = True
    if a[i] < a[i+1]:
        is_asc = True

if is_asc and is_desc:
    print('Lista desordenada')
elif not is_asc and is_desc:
    print('Lista con elementos iguales')
elif is_asc and not is_desc:
    print('Lista con orden ascendente')
elif is_desc and not is_asc:
    print('Lista con orden descendente')

