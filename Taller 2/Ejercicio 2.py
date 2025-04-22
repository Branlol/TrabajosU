#2. Construir un programa que tome una cadena de caracteres e imprima todas la posibles permutaciones de los 
#mismos.  Antes de construirlas, el programa deberá limpiar posibles caracteres repetidos de la cadena.  Se 
#deberá obtener un número N de elementos que se toman, y se debe tener en cuenta el número M de posibles 
#valores, es decir, el número de caracteres diferentes en la cadena dada.  Por ejemplo:
# cadena de entrada: abcfga
# elementos que se tienen en cuenta: abcfg
# permutaciones:
# abcfg
# abcgf
# abgfc
# …
def quitarpalabra(n):
    res = ""
    for i in range(len(n)):
        if n[i] not in res:
            res += n[i]
    return res

def permutac(n, l=0):
    if l == len(n):
        print("".join(n))
    else:
        for k in range (l,len(n)):
            n[l], n[k] = n[k], n[l]
            permutac(n, l+1)
            n[l], n[k] = n[k], n[l]


palabra = str(input("Ingresa la cadena:\n"))

lol = quitarpalabra(palabra)
print(lol)
resul = permutac(list(lol))
print(resul)