a = [123,43, 312,4, 54, 654, 121, 78, 9]

num_max = 0
for i in range(len(a)):
    if a[i] > num_max:
        num_max = a[i]

print(num_max)