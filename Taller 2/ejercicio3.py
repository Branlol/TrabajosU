#4. Un número es un cuadrado perfecto si su raíz cuadrada es un número exacto (sin decimales). Por ejemplo, 
#el 4 es un cuadrado perfecto (2²), al igual que lo son el 36 (6²) y el 3.500.641 (1871²).
# Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo. Por 
#ejemplo, el número 8 no es un cuadrado perfecto, pero al multiplicarlo por 2 se obtiene el 16, que sí lo es. 
#Entradas del programa: La entrada comienza con un número que indica cuántos casos de prueba tendrán que 
#procesarse.  Cada caso de prueba consiste en un número mayor que 0 y menor que 231. 
#Salidas: Para cada caso de prueba, el programa escribirá por la salida estándar, en una línea independiente, el 
#número más pequeño que al ser multiplicado por el número del caso de prueba da como resultado un 
#cuadrado perfecto. 
import math
n = int(input("Ingrese al numero al que le hallaremos el cuadrado perfecto:\n"))
salida = False
raizcheck = math.sqrt(n)
if raizcheck == int(raizcheck):
    salida = True
    print("El numero es un cuadrado perfecto")
numv = 0
while salida == False:
    numv += 1
    checker = math.sqrt(n * numv)
    if checker == int(checker):
        salida = True
        print(f"El numero por el que se debe multiplicar es {numv}")



    



