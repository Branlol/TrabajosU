#Escribir un programa que reciba una entrada n, que es un número entero. El programa devolverá una 
#lista de números enteros hasta n, incluyéndolo, y especificando si el número es divisible por 2, 3 o por 
#5, o si es divisible por ambos. 

numero = int(input("Ingrese un numero:\n"))

for i in range(1, numero+1):
    Divisores = ""
    if i % 2 == 0:
        Divisores = "2"
    if i % 3 == 0:
        Divisores = Divisores + ", 3"
    if i % 5 == 0:
        Divisible5 = True
        Divisores = Divisores + ", 5"
    
    if Divisores == "":
        print(f"{i}.")
    else:
        print(f"{i}. Divisible por: {Divisores}")
    
