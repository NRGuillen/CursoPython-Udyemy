a = [0] * 10
b = [0] * 10
c = [0] * 20

for i in range(len(a)):
    a[i] = i + 1

for i in range(len(b)):
    b[i] = (i + 1) * 5

# INSERCION EN LISTA C DE 2 EN 2
aux = 0
for i in range(0, len(a),2):
    for j in range(2):
        c[aux] = a[i+j]
        aux+= 1

    for j in range(2):
        c[aux] = b[i+j]
        aux+= 1

for i in c:
    print(i)
