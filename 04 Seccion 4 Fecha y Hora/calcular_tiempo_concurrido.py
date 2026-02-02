import time

# Se utiliza para medir tiempos, como un conometro, es la mejor opcion para hacer mediciones de tiempo
inicio = time.perf_counter()
time.sleep(1.5)
final = time.perf_counter()

print(f'Tiempo total concurrido: {final - inicio} segundos') #1.50048660000175
print(f'Tiempo total concurrido: {final - inicio:.2f} segundos') #1.50