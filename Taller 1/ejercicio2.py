#Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el
# número primo de valor más cercano, en este caso menor o igual, al número leído.

valor = False
while valor == False: #En este while miramos si el entero es mayor a 2
 numer = int(input("ingrese un valor mayor a 2:\n"))
 if numer > 2:
        valor = True
 else: 
        print("El valor no es mayor a 2")
k = 0
primo = False

while primo == False: #En este bucle buscamos el primo mas cercano y cuando lo encontramos cortamos el while
  Divisores = 0
  for i in range(numer,2,-1):
    if numer % i == 0:
      Divisores = Divisores + 1

    if i == 3 and Divisores == 1:
      Valor = numer
      primo = True
      print(f"{Valor}")
      
  numer = numer - 1
    
    


      
  




 