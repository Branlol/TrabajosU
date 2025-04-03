# Escribir un programa que determine si un número entero es positivo, negativo o cero. Después, 
#modificar el programa para que reciba entradas de números enteros hasta que el número introducido 
#sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.
Run = False
Promediop = 0
Promedion = 0
Quann = 0
Quanp = 0
valores = 0
while Run == False:
    numero = int(input("Ingrese un numero entero:\n"))
    if numero > 0:
        positivo = True
        Quanp = Quanp + 1
        print("El valor ingresado es positivo")
    elif numero == 0:
        Run = True
        print("El valor ingresado es cero")
    else:
        Quann = Quann + 1
        print("El valor ingresado es negativo")
    valores = valores + 1

FPromediop = (Quanp / valores)*100
FPromedion = (Quann / valores)*100

print(f"En total ingresaste {valores} numeros, entre ellos {Quanp} positivos, {Quann} negativos y el cero. Es decir un {FPromediop}% fueron positivos y un {FPromedion}% fueron negativos ")