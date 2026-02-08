numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numeros) // 2):
    print(numeros[i])
    print(numeros[len(numeros) - i - 1])
    print('=========')
