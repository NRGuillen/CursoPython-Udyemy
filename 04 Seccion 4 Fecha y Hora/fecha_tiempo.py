import datetime
import locale

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252') # Para que el mes salga en español

hoy = datetime.date.today()
print(f'Hoy es: {hoy}')
print(f'Año: {hoy.year}')
print(f'Mes: {hoy.month}')
print(f'Dia: {hoy.day}')

fecha_cumpleanos = datetime.date(2005, 2, 13)
print(f'Mi cumpleaño es: {fecha_cumpleanos}')

ahora = datetime.datetime.now() # año, mes, dia, horas, minutos, segundos, milisegundos
print(ahora)

date_time = datetime.datetime(2019, 4, 17, 14,55,59, 8797)
print(date_time)

formato_fecha = date_time.strftime('%d-%m-%Y %H:%M') # Dia, Mes, Año, Hora, Minutos
print(formato_fecha)

formato_fecha = date_time.strftime('%d de %B, %Y') # Dia, Mes con nombre, Año
print(formato_fecha)

