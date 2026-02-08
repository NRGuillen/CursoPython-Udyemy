a = [0] * 10
b = [0] * 10
c = [0] * 20

for i in range(len(a)):
    a[i] = i + 1

for i in range(len(b)):
    b[i] = (i + 1) * 5

c =  a + b

for i in c:
    print(i)

print('=========')
c = [0] * 20

aux = 0
for i in range(len(a)):
    c[aux] = a[i]
    aux+= 1
    c[aux] = b[i]
    aux+= 1

for i in c:
    print(i)
