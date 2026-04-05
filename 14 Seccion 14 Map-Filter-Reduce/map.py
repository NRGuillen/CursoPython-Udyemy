
numbers = [1,2,3,4,5,6,7]

# Con map
numberx2 = list(map(lambda num : num *2, numbers)) # [2, 4, 6, 8, 10, 12, 14]
print(numberx2)

# Sin map
numeros_pares = [x * 2 for x in numbers]