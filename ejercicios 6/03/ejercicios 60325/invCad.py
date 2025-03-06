entrada = input("Palabra a voltear: ")
n = len(entrada)
salida = ""

for i in range(n) :
    print(entrada[i])
    salida = entrada[i] + salida
    print(salida)
print(salida)
    
