import numpy as np

matriz = np.array([[-2,4,5],[6,7,-3],[3,0,2]])

lin1 = matriz[0,:].reshape(1,-1)#Con ese -1 va a dejar de ser un array de 3 elementos, a ser un array de 3 columas
lin2 = matriz[1,:].reshape(1,-1)

ma = np.concatenate((matriz,lin1,lin2), axis=0) #El axis es para saber si se unen en filas o columnas, 0 para filas
det = 0


lol = 0
for k in range(3):#Filero
    coso = 1
    j = k - 1
    
    for i in range((ma.shape[1])):#Columnero
        j += 1
        coso = coso * ma[j][i]
    lol = lol + coso

for k in range(3):#Filero
    coso = 1
    j = k - 1
    
    for i in range(2,-1,-1):#Columnero
        j += 1
        coso = coso * ma[j][i]
    lol = lol - coso
print(lol)