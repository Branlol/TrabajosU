#Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras 
#del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0.  Por ejemplo:
# 12345 → 23456.
#987654 → 098765.
numero = int(input("Ingrese un numero:\n"))
Final = ""
numero = str(numero)
lol = len(numero)
for i in range(lol):
    valor   = numero[i]
    valor = int(valor)
    Final1 = 0
    if valor == 9:
        Final = Final + "0"
    else:
            Final = Final + str((valor + 1))
print(Final)