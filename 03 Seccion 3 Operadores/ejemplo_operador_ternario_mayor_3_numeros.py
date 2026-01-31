
num1 = int(input('Ingese un numero: '))
num2 = int(input('Ingese un segundo numero: '))
num3 = int(input('Ingese un tercer numero: '))
num4 = int(input('Ingese un cuarto numero: '))

max = num1 if num1 > num2 else num2
max = max if max > num3 else num3
max = max if max > num4 else num4

print(max)

