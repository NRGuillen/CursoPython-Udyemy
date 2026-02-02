
text = 'Hola'
if text:
    print('Pasa porque el texto no esta vacio')

text = ''
if text: # No se ejecuta pq esta vacio
    print('pasa o no pasa')

personas = ['Ruben', 'Aitor']
if personas:
    print('Pasa pq tiene personas')

if personas is not None:
    print('No esta vacio')
else:
    print('Esta vacio')

personas = None # Tiene que ser None, para que entre en el else, si es una array vacio no entraria al else
if personas is not None:
    print('No esta vacio')
else:
    print('Esta vacio')
