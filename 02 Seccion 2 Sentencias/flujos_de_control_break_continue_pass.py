print('========= Break')
for number in range(10):
    if number == 5:
        break # Para el flujo del for
    print(number)

print('========= Pass')
for number in range(10):
    if number == 5:
        pass # No sirve para nada, simplemente para marcar que tenemos que hacer algo en esa linea de codigo
    print(number)


print('========= Continue')
for number in range(10):
    if number == 5:
        continue # Se salta el numero 5
    print(number)

users = ['Andrea', 'Pedro', 'Anonimo', 'Diego']

for nombres in users:
    if nombres == 'Anonimo':
        print('Usuario restringido')
        continue
    print(f'Bienvenido {nombres}')