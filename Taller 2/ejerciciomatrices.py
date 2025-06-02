import numpy as np
n = int(input("Ingrese el nxn de tu matriz cuadradad:\n"))
matriz = []
for i in range(n):
    l = []
    for k in range(n):
        numtemp = int(input(f"Ingrese el valor de la fila{i+1} de la columna {k+1}:\n"))
        l.append(numtemp)
    matriz.append(l)

print(matriz)
    
superior = True
inferior = True

for i in range(n):
    for j in range(n):
        if i > j and matriz[i][j] != 0:
            superior = False
        if i < j and matriz[i][j] != 0:
            inferior = False

if superior or inferior:
    print("SI: La matriz es triangular.\n")
else:
    print("NO: La matriz no es triangular.\n")
