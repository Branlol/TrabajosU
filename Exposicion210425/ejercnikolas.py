#Juan Londoño
#Nikollas Mendoza
#Samuel Becerra
#Brandon Jaimes
pasar = False
n = []
l = 1
print("Ingrese la cantidad de numeros que usted desee,para dejar de escribir numeros escriba -10")
def insertion_sort(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
        i += 1
    return L
def busqueda_binaria(lis, obj):
    izquierda, derecha = 0, len(lis) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lis[medio]
        print(f"izquierda={izquierda}, derecha={derecha}, medio={medio}, valor medio={valor_medio}")

        if valor_medio == obj:
            return medio
        elif valor_medio < obj:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None  # El objetivo no está en la lista

while pasar == False:
    k = int(input(f"Ingrese el numero {l} de la lista:\n"))
    l += 1
    if k == -10:
        pasar = True
    else:
        n.append(k)

print (n)
n = insertion_sort(n)
print(n)
v=int(input("inserte el valor a buscar: "))
print(busqueda_binaria(n,v))#Modificar solo el numero a buscar



"""def busqueda_binaria_recursiva(lista, objetivo, izquierda, derecha): #Recursividad
    if izquierda > derecha:
        return -1  # Caso base: el objetivo no está en la lista

    medio = (izquierda + derecha) // 2

    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, izquierda, medio - 1)"""