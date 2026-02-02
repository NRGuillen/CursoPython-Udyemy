import datetime

texto = '17-04-2025 18:30'

fecha = datetime.datetime.strptime(texto, '%d-%m-%Y %H:%M')
print(fecha)

fecha_str = '17 april, 2025'
fecha = datetime.datetime.strptime(fecha_str,'%d %B, %Y')
print(fecha.year)