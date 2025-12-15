num_values = 10

a = 0
print(a)
b = 1
print(b)

for _ in range (num_values -2):
    r = a + b
    a = b
    b = r
    print(r)