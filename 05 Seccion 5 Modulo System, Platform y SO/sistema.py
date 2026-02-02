import datetime
import sys

# La unica diferencia es que el print hace salto de linea \n y el sys.stdout no
print('Hola mundo')
sys.stdout.write('Hola mundo, desde system.out\n')
sys.stderr.write('Mensaje de error en rojo\n')

try:
    date = datetime.datetime.strptime('2026-02-02', '%Y-%m-%d')

except ValueError as err:
    sys.stderr.write(f'Error con el formato de fehca {err}\n')
    sys.exit(1) # Salida de error