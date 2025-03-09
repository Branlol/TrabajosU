Palabra = input("Ingrese la palabra que desea pasar a piglatin:\n")
Largo = len(Palabra)
if Palabra[0] == " ":
    Palabra = Palabra[1:Largo]
    Largo = len(Palabra)
else:
    if Palabra[0].lower() in "aeiou":
        Resultado = Palabra + "yay"
    else:
        Resultado = Palabra[1:Largo] + Palabra[0] +"ay"

    print(Resultado)
    

