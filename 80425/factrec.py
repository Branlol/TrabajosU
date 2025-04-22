def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("n: "))
print(fact(n))