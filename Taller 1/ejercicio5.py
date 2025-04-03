#Escribir un programa que permita convertir un entero dado en base 2, 4, 8, 16.
negativo = False
pasar = False
listo = False
lol = int(input("Introduce un numero entero: \n"))

base = 2
y = 1
while base < 9:
    listo = False
    
    k = 0
    Final = 0
    y = y + 1
    numero = lol
    while listo == False:
       
        casi = numero % base
        numero = int(numero / base)
        potencia = 10**k
        Final = Final + (potencia*casi)
        k = k + 1
        if numero < base:
            potencia = 10**k
            Final = Final + (potencia * numero)
            
            print(f"{Final} es el valor en base {base}")
            listo = True
    base = 2**y



base = 16
    
k = 0#FALTA ARREGLAR CUANDO ES BASE 16
Final = ""
numero = lol
listo = False
while listo == False:

    casi = numero % base
    numero = int(numero / base)
    if casi == 10:
        casi = "A"
    elif casi == 11:
        casi = "B"
    elif casi == 12:
        casi = "C"
    elif casi == 13:
        casi = "D"
    elif casi == 14:
        casi = "E"
    elif casi == 15:
        casi = "F"
    casi = str(casi)
    
    Final = casi + Final
    if numero < base:
        Final = str(numero) + Final
            
        print(f"{Final} es el valor en base {base}")
        listo = True



    
        
    
        
