def submatriz(matriz,fila,columna):
    subm = []
    for i in range(len(matriz)):#Miro la can de filas
        if i == fila:
            continue #Me salto esta iteracion

        n_fila = []
        for j in range(len(matriz[i])):#El j es para recorrer la fila esp
            if j == columna:
                continue#Me salto la iteracion
            n_fila.append(matriz[i][j])
        subm.append(n_fila)
    return subm

def determinantelol(matriz):
    if len(matriz) == 2:
        return((matriz[0][0]*matriz[1][1])-(matriz[0][1]*matriz[1][0]))
    det = 0 
    for col in range(len(matriz)):
        sub = submatriz(matriz,0,col)#En la siguiente line a esta, se eleva a col para lo de las posiciones
        cofact = ((-1)**col) * matriz[0][col] * determinantelol(sub)#Se le saca determinante hasta convertir en 2x2
        det += cofact
    return det
matriz = []
print("bienvenidololol")
n = int(input("Ingrese el n de nxn de la matriz"))
for x in range(n):
    mba = []
    for y in range(n):
        mba.append(int(input(f"Ingrese el valor de la fila{x+1}, en la columna {y+1}:\n")))
    matriz.append(mba)
        
print(f"Su matriz es {matriz}")
print(f"El determinante de su matriz es:{determinantelol(matriz)}")