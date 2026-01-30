notas_5 = 0
notas_4 = 0
notas_1 = 0
promedio = 0.0
error = False

for i in range(0,20):
    nota = float(input(f'Introduce la {i + 1}º nota: '))

    if nota <= 0 or nota > 7:
        error = True
        break

    if nota >= 5:
        notas_5 += 1
    elif nota <= 4 and nota > 1:
        notas_4 += 1
    elif nota == 1:
        notas_1 += 1

    promedio += nota

if not error:
    print(f'Notas mayores a 5: {notas_5}/20')
    print(f'Notas menores a 4: {notas_4}/20')
    print(f'Notas igual a 1: {notas_1}/20')
    print(f'Promedio de las 20 notas: {promedio / 20}/20')
else:
    print('Error al introducir notas ')


