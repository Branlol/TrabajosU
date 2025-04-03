#Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro 
#entero, o sea, que tiene raíz cuadrada entera.

numero = int(input("Ingrese un entero positivo: \n"))
Raices = False
for i in range(0,numero):
    if i*i == numero:
        Raices= True

if Raices == True:
    print(f"El numero tiene raiz entera")
else: 
    print(f"El numero no tiene raiz entera")