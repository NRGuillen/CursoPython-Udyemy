"""Para esta tarea se pide ingresar una fecha de nacimiento en formato string, convertirla a una fecha date y calcular
la edad de la persona de acuerdo a la fecha actual."""
import datetime

def formateo_fecha(fecha_str):
    fecha = datetime.datetime.strptime(fecha_str, '%d-%m-%Y')
    return fecha

try:
    ano_actual = datetime.datetime.now()
    ano_nacimiento = input(f'Introduce la fecha de tu naciminento con el siguiente formato "dd-mm-yyyy": ')
    ano_nacimiento = formateo_fecha(ano_nacimiento)
    print(f'Tienes {int(ano_actual.year) -int(ano_nacimiento.year)} años')

except ValueError as err:
    print(f'Has introducido un formato de fecha erroneo: {err}')