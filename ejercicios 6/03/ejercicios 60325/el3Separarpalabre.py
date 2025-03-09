Frase = input("Ingrese una frase:")
max = len(Frase)
parte = ""
for i in range(max):
    if (Frase[i]) == " ":
        print(parte)
        parte = ""
    else:
        parte =  parte +(Frase[i]) 

print(parte)