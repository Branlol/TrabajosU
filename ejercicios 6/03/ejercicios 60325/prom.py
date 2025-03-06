n = int(input("Número de elementos: "))
suma = 0
for i in range(n):
    elem = float(input(f"Valor del elemento {i}: "))
    suma = suma + elem

if n > 0 :
    promedio = suma / n
    print(promedio) 
else :
    print("Número de elementos inválido")