fibonacci = 100

n1 = 0
n2 = 1
n3 = n1 + n2

for i in range(fibonacci):
    n3 = n1 + n2
    n2 = n1
    n1 = n3

print(n3)