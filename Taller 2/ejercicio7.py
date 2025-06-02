#8. Escribir un programa que pida números enteros positivos y los convierta en romanos. El programa debe 
#pedir números enteros hasta que se introduzca un 0, lo que detiene el ciclo.
def entero_a_romano(num):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""
    for valor, simbolo in valores:
        while num >= valor:
            romano += simbolo
            num -= valor
    return romano
pasar = False

while pasar == False:
    N = int(input("Ingrese un numero positivo"))
    if N > 0:
        pasar = True

print (entero_a_romano(N))

