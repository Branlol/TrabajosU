#Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor 
#entero dado por el usuario.
numero = int(input("Ingrese un numero:\n"))
penultimo = 0
ultimo = 1
finalb = False
while finalb == False:
    suma = ultimo + penultimo
    penultimo = ultimo
    ultimo = suma
    if penultimo >= numero:
        print(ultimo)
        finalb = True
