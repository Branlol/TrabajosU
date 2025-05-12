n = int(input("Introduzca n: "))
nbak = n
m = 0
s = 0
factor = 1
while n > 0 :
    r = n % 10
    n = n // 10
    m = r * factor + m
    factor = factor * 100

print(m)

