#Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo 
#común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común 
#múltiplo.
Par = False 
n2mayor = False
terminado = False
n1 = int(input("Ingrese el primer numero:\n"))
n2 = int(input("Ingrese el segundo numero:\n"))

if (n1+n2)% 2 == 0:
    Par = True
    if n2 > n1:
        n2mayor = True
i = n2
if Par == True:
    while terminado == False:
        
        if n2 % i == 0 and n1 % i == 0:
            terminado = True
            print(i)
        i = i - 1

if Par == False:
    num = n1*n2
    while terminado == False:
        if n2 % i == 0 and n1 % i == 0:
            terminado = True
            dem = i
        i = i-1
    Resultado = num / dem
    print(Resultado)