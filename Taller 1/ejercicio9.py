#Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a 
#un valor entero dado por el usuario.
numero = int(input("Ingrese un numero:\n"))
penultimo = 0
ultimo = 1
finalb = False
while finalb == False:
    suma = ultimo + penultimo
    penultimo = ultimo
    ultimo = suma
    if ultimo > numero:
        print(penultimo)
        finalb = True

