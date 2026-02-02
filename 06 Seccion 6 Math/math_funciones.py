import math

# OBTENER EL NUMERO SIN SU SIGNO
absoluto = abs(-3) # El absoluto devuelve el numero, independientemente de su signo, simplemente el numero solo
print(absoluto) # 3
absoluto = abs(5)
print(absoluto) # 5

# MINIMO Y MAXIMO ENTRE NUMEROS
maximo = max(1.0,43, 5.3, 123, 432) # Retorna el numero maximo entre x numeros
print(maximo) # 432
minimo = min(1.0,43, 5.3, 123, 432) # Retorna el numero minimo entre x numeros
print(minimo) # 1.0

# REDONDEO DE NUMEROS
redondear_numero_hacia_arriba = math.ceil(3.1) # Redondea hacia arriba siempre, aunque sea 3.1
print(redondear_numero_hacia_arriba) # 4
redondear_numero_hacia_abajo = math.floor(3.9) # Redondea hacia abajo siempre, aunque sea 3.9
print(redondear_numero_hacia_abajo) # 3
renondear_numero_normal = round(3.5) # Redondea hacia arriba si es >= 3.5 o hacia abajo <= 3.4
print(renondear_numero_normal) # 4

# NUMERO PI
print(math.pi)

# EXPONENTE DE E
print(math.e)

exponente = math.exp(1) # Vamos a elevar E (la constante exponencial) a 1
print(exponente)
exponente = math.exp(3) # E^3
print(exponente)

# ELEVAR NUMEROS
print(math.pow(3, 3))

# RAIZ CUADRADA
raiz_cuadrada = math.sqrt(5)
print(raiz_cuadrada)

# GRADOS
grados = math.degrees(1.57) # Corresponde a 90 grados en radianes
print(grados)

# RADIANES
radianes = math.radians(90.00) # Corresponde a 1.57 en grados
print(radianes)

# SENO
print(math.sin(radianes)) # Seno de 90 grados = 1

# COSENO
print(math.cos(radianes))



