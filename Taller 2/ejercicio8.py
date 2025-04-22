#9. Dada una lista de enteros y una suma objetivo, escriba una función que imprima todos los pares únicos de 
#elementos de la lista que suman la cantidad objetivo. Cada par debe imprimirse en una línea nueva en el 
#formato a, b, y no deben contarse pares duplicados. La entrada consiste en una lista de enteros (por ejemplo, 
#[1, 2, 3, 4, 3, 5, 6]), y un número entero que representa la suma objetivo (por ejemplo, 7).  La salida debe ser 
#todos los pares únicos de números que suman el valor objetivo. Cada par se debe imprimir en una línea nueva 
#en el formato a, b. Los mismos dos números en un orden diferente no deben aparecer nuevamente, por 
#ejemplo:
# 1, 6
# 3, 4
# 2, 5

N = int(input("Ingrese la cantidad de val que va a tener la lista\n"))
lnum = []
for i in range(N):
    lnum.append(int(input(f"Ingrese el valor {i+1}:")))
Obj = int(input("Ingrese ahora la cantidad objetivo de suma:\n"))
checker = []
for i in range(N):
    for k in range(N):
        if (lnum[i] + lnum[k]) == Obj:
            if (int(str(lnum[i]) + str(lnum[k]))) not in checker:
                print(str(lnum[i]) + "," + str(lnum[k]))
                checker.append(int(str(lnum[i]) + str(lnum[k])))
                checker.append(int(str(lnum[k]) + str(lnum[i])))