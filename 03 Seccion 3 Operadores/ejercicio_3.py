"""Instrucciones de tareas

Obtener el nombre mas largo de tres personas, según los siguientes requerimientos

Mediante tres miembros de la familia o amigos.

-Calcular e Imprimir el nombre de la persona que tenga el nombre más largo (en cantidad de caracteres) 
 (Imprimir sólo uno de los tres, el de más caracteres en el nombre.)
-Podría usar .split(" "); del objeto str para separar nombre y apellido en un arreglo, y con el indice 
 cero accedemos al nombre de la persona.
-Restricción no usar loops en el desarrollo de la tarea.

Ejemplo del resultado: "Guillermo Doe tiene el nombre más largo."""

nombre1 = 'Ruben Guillen'
nombre2 = 'Sara Garcia'
nombre3 = 'Marta Yul'

nombre_largo = None

if len(nombre1.split(' ')[0]) >= len(nombre2.split(' ')[0]):
    nombre_largo = nombre1
else:
    nombre_largo = nombre2

if len(nombre_largo.split(' ')[0]) < len(nombre3.split(' ')[0]):
    nombre_largo = nombre3

print(f'El nombre mas largo es: {nombre_largo}')

# Solucion Profesor

persona1 = "Juan Perez"
persona2 = "Maria Lopez"
persona3 = "Andres Guzman"

max_persona = persona2 if len(persona1.split(" ")[0]) < len(persona2.split(" ")[0]) else persona1
max_persona = max_persona if len(persona3.split(" ")[0]) < len(max_persona.split(" ")[0]) else persona3

print("La persona con el nombre más largo es", max_persona)
