import random as rnd
import math
def media(k):
    MediaA = sum(k)/len(k)
    return MediaA

def varianza(k):
    n = []
    for i in range(len(k)):
        n.append((k[i]-media(k))**2)
    Vara = (sum(n)/(len(k)-1))
    return Vara

def desviestand(k):
    n = []
    for i in range(len(k)):
        n.append((k[i]-media(k))**2)
    
    desvs = math.sqrt((sum(n))/len(k)-1)
    return desvs
    
def rang(k):
    rango = max(k)-min(k)
    return rango
        

n = int(input("Ingrese la cantidad de valorws de la lista papu:\n"))

A = []
B = []
for i in range(n):
    A.append(rnd.randint(1,100))
    B.append(rnd.randint(1,100))


print(f"En el caso de la lista A su Media es {media(A)}, su varianza es {varianza(A)}, su desviacion estandar es {desviestand(A)}, su rango es {rang(A)}. \n")

 
print(f"En el caso de la lista B su Media es {media(B)}, su varianza es {varianza(B)}, su desviacion estandar es {desviestand(B)}, su rango es {rang(B)}. \n")


