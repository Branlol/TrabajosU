#Construir un programa que lea un número variable de valores enteros. El resultado que entregara el 
#programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores 
#pares dividida por el número de estos. 
Den = int(input("Ingrese la cantidad de valores con los que desea realizar la media:\n"))
num = 0
lol = 0
for i in range(Den): #Aca usamos un for para leer todos los valores que van en el numerador
 Val = int(input(f"Ingrese el valor {i+1}:\n"))
 if Val % 2 == 0: #Aca miramos que valores son pares
    num = num + Val
    lol = lol + 1
    

resultado = num / lol 
print(f"El resultado es {resultado}")