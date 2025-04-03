import random as rnd
import math as mata
n = int(input("Ingrese la cantidad de valorws de la lista papu:\n"))

A = []

for i in range(n):
    A.append(rnd.randint(1,100))

for j in range(len(A)):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            print(A)