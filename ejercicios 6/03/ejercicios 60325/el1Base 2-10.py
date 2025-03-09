negativo = False
pasar = False
listo = False
numero = int(input("Introduce un numero entero: \n"))
if numero < 0: #Borrar en caso de no necesitarse pasar a positivo para el 
    negativo = True
while pasar == False:
    base = int(input("Escribe una base a la que quieras pasar el numero entre 2 y 10:\n " ))
    if base >=2 and base <10:
        pasar = True
    else :
        print("Base incorrecta")
k = 0
Final = 0

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
    
    
        


    




    









        
        


