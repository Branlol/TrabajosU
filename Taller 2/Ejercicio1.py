#1. Construir un programa que permita cifrar y descifrar una frase usando el cifrado conocido coloquialmente 
#como el cifrado de César.  Este cifrado consiste en reemplazar cada letra de un texto por la letra que está tres 
#posiciones adelante en el alfabeto, por ejemplo cambiar todas las “A” por “D”; este valor de tres, para tres 
#posiciones del alfabeto, lo llamaremos valor de salto, y puede variar.  Este programa debe hacer algo más: 
#usar el valor de salto de 3 para las palabras en posiciones pares y el valor de salto de 4 para las que estén en 
#posiciones impares.  El programa naturalmente tomará los espacios en blanco como separador de palabras y 
#los ignorará para el proceso de reemplazo, al igual que los signos de puntuación.
Resultado = ""
pasar = False
while pasar == False:

    print("Bienvenido al programa de cifrado de Cesar")
    print("Tienes las siguientes opciones \n 1.Cifrar \n 2.Descifrar")
    Elec = int(input("Por favor ingrese el numero de la opcion a realizar:\n"))
    if Elec == 1 or Elec == 2: #Se verifica si la opcion es correcta o no
        pasar = True
    else: 
        print("El numero ingresado no es valido. Se reiniciara......")

    palabra = str(input("Ingrese la palabra:\n"))
    if Elec == 1: #Se realiza el proceso de cifrado
        for i in range(len(palabra)):#Para evaluar cada palabra
            newword = ord(palabra[i])
            if newword >= 65 and newword <=90:#Evaluamos cuando es mayuscula
                if i % 2 == 0: #Evaluamos en las mayus si es impar
                    newword = newword + 4 #Se le suma a la posiccion ASCII 4
                    if newword > 90: #Si se excede la palabra vuelve a la posicion inicial de las ASCII y se le suma ahi
                        dif = newword - 90
                        newword = 65 + dif
                    newword = chr(newword)# Convertimos a palabra normal nuevamente
                    Resultado = Resultado + newword
                else: #Evaluamos cuando es par
                    newword = newword + 3
                    if newword > 90: #Miramos si la palabra excede posicion ASCII y si es asi la devolvemos a el 1st valor ASCII
                        dif = newword - 90
                        newword = 65 + dif
                    newword = chr(newword) #Convertimos a palabra normal
                    Resultado = Resultado + newword
            elif newword >= 97 and newword <=122: #Ahora evaluamos cuando es minuscula
                if i % 2 == 0: #Se evalua si es impar
                    newword = newword + 4
                    if newword > 122: #Se mira si se excede
                        dif = newword - 122
                        newword = 97 + dif
                    newword = chr(newword) #Se convierte
                    Resultado = Resultado + newword
                else: #Evaluamos cuando son pares
                    newword = newword + 3
                    if newword > 122: #Verificamos si excede
                        dif = newword - 122
                        newword = 97 + dif
                    newword = chr(newword) #Convertimos de nuevo
                    Resultado = Resultado + newword
            elif newword == 32:
                Resultado = Resultado + " "
    elif Elec == 2: #Ahora evaluamos el proceso de descifrado
        for i in range (len(palabra)):#Para recorrer cada palabra
            newword = ord(palabra[i])
            if i % 2 == 0: #Evaluamos si es impar
                if newword >= 65 and newword <=90: #Evaluamos si es mayus
                    newword = newword - 4
                    if newword < 65: #Miramos si se excedio y convertimos a max ASCCII
                        dif = 65 - newword
                        newword = 90 - dif
                elif newword >= 97 and newword <=122:#Evaluamos las minus
                    newword = newword - 4
                    if newword < 97: #Miramos si se excedio y convertimos a min ASCII
                        dif = 97 - newword
                        newword = 122 - dif
            else:
                if newword >= 65 and newword <=90: #Same process solo que cuando la posicion es par
                    newword = newword - 3
                    if newword < 65:
                        dif = 65 - newword
                        newword = 90 - dif
                elif newword >= 97 and newword <=122:
                    newword = newword - 3
                    if newword < 97:
                        dif = 97 - newword
                        newword = 122 - dif
            newword = chr(newword)
            Resultado = Resultado + newword






print(Resultado)
#chr(numero)
#ord(letra)