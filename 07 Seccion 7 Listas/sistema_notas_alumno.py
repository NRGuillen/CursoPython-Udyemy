clase_matematicas = [0.0] * 7 # 7 Alumnos
clase_lengua = [0.0] * 7
clase_hisoria = [0.0] * 7

suma_notas_mates = 0
suma_notas_leguaje = 0
suma_notas_historia = 0

print('Ingrese 7 notas de estudiantes para Matematicas')
for i in range(7):
    clase_matematicas[i] = float(input(f'Nota {i+1}:'))
    suma_notas_mates += clase_matematicas[i]

print('Ingrese 7 notas de estudiantes para Lengua')
for i in range(7):
    clase_lengua[i] = float(input(f'Nota {i+1}:'))
    suma_notas_leguaje += clase_lengua[i]

print('Ingrese 7 notas de estudiantes para Historia')
for i in range(7):
    clase_hisoria[i] = float(input(f'Nota {i+1}:'))
    suma_notas_historia += clase_hisoria[i]

print(f'Promedio total del curso: {(suma_notas_mates + suma_notas_leguaje +suma_notas_historia) / 3: .2f}')
print(f'Notas matematicas: {suma_notas_mates / 7 : .2f}')
print(f'Notas lenguaje: {suma_notas_leguaje / 7: .2f}')
print(f'Notas historia: {suma_notas_historia / 7: .2f}')

id_alumno = int(input('Introduce el id del estudiante, para ver sus notas(1-7):')) - 1
print(f'Alumno[{id_alumno}]: Matematicas: {clase_matematicas[id_alumno]}, Lenguaje: {clase_lengua[id_alumno]}, Historia: {clase_hisoria[id_alumno]}')
print(f'Su promedio es: {(clase_matematicas[id_alumno] + clase_lengua[id_alumno] + clase_hisoria[id_alumno]) / 3: .2f}')

# SISTEMA OPTIMIZADO

asignaturas = ['Matematicas', 'Historia', 'Lenguaje']
estudiantes = 7
notas_por_asignaturas = [] # Matriz

for asignatura in asignaturas:
    notas = [float(input(f'Nota {i + 1} para {asignatura}: ')) for i in range(estudiantes)]
    notas_por_asignaturas.append(notas)
    print('=====')

print('Promedios por asignatura')
promedios_asignaturas = []

for asignatura, notas in zip(asignaturas,notas_por_asignaturas): # Combina 2 arreglos como si fuera solo 1 iteracion, ambos arrays tienen que tener el mismo tamaño
    promedio = sum(notas) / len(notas)
    promedios_asignaturas.append(promedio)
    print(f'{asignatura}: {promedio:.2f}')

promedio_total = sum(promedios_asignaturas) / len(promedios_asignaturas)
print(f'Promedio total del curso: {promedio_total}')
try:
    alumno_id = int(input('Introduce el id del estudiante, para ver sus notas(1-7):')) - 1

    notas_estudiante = [notas[alumno_id] for notas in notas_por_asignaturas]
    promedio_alumno = sum(notas_estudiante) / len(notas_estudiante)
    print(f'Promedio del Alumno[{alumno_id}]: {promedio_alumno}')
except ValueError:
    print('Entrada invalida. Debe ser un numero entero')