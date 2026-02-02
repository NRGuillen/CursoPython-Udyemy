"""La tarea consiste en crear un nuevo archivo llamado detalle_de_factura.py, que contenga una función principal (main)
 donde desarrolles un programa que simule la creación de una factura.

En esta versión no se utilizará la función input() (ya que en algunos entornos de prueba online no está disponible).

En su lugar, los valores se deben asignar directamente en el código mediante variables.

Requisitos:

    Definir el nombre o descripción de la factura
        Asigna un texto directamente a una variable.

    Definir los precios de dos productos de tipo decimal
        Asigna valores numéricos con decimales usando float.

    Calcular los totales
        Suma ambos precios para obtener el total bruto, calcula el impuesto del 19% sobre ese total y finalmente el
        total neto (bruto + impuesto).

    Mostrar los resultados
        Se debe imprimir en una sola línea (print) el nombre de la factura, el total bruto, el impuesto y el total neto.

Ejemplo de salida esperada:
La factura Productos de oficina tiene un total bruto de 134.78, con un impuesto de 25.6082 y el monto después de
impuesto es de 160.3882

IMPORTANTE:
Todas las tareas publicadas en el curso son opcionales.
No afectan tu progreso, el temario ni la entrega final del diploma o reconocimiento por haber completado el curso.
Son actividades 100% opcionales y cada una incluye su correspondiente código de solución.
La plataforma de Udemy no marca las tareas como completadas (“checked”) al realizarlas.
Esto es una característica propia del sistema de Udemy, y no depende del curso ni del instructor."""

descripcion = 'Ordenadores de oficina para desarrollar aplicaciones multiplataforma'
precio = 1233.21
impuesto_españa = 21

impuesto = (precio * impuesto_españa) / 100

output = (f'La factura de "{descripcion}" tiene un total bruto de {precio}, con un impuesto de {impuesto}, sumando un total'
          f' de : {impuesto}')
print(output)