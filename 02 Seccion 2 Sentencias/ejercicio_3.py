"""Se pide dos números enteros positivos o negativos, pero sin usar el símbolo de multiplicación (*).

Puede utilizar una sentencia for para realizar la multiplicación y tener en cuenta los unarios, donde menos por
menos es positivo."""

num_1 = -6
num_2 = 13
resultado = 0

if num_1 < 0:
    num_1 = str(num_1)[1:]
if num_2 < 0:
    num_2 = str(num_2)[1:]

for i in range (int(num_1)):
    resultado += int(num_2)

print(resultado)
