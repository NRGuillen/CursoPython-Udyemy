name = 'Ruben Guillen'
age = 20
text = f'Me llamo {name} y tengo {age} años'
print(text)

a = 5
b = 3
print(f'La suma de a y b es: {a + b}')

price = 51
print(f'Este producto es muy {'Caro'if price > 50 else 'Barato'}')

text = 'El precio es {price} dolares'
print(text.format(price = 51))

text = 'Oferta por solo {price:.2f} dolares'
print(text.format(price = 51))
