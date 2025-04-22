import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

com = int(input("Ingrese 1 si desea y de tiempo, si no ingrese cualquier valor para y de Op: \n"))

def bubble_sort(A): #green
    cb = 0
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            cb += 1
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                cb += 1
            
    return A, cb

def insertion_sort(A): #blue
    ci = 0
    i = 1
    while i < len(A):
        j = i
        ci += 1
        while j > 0 and A[j - 1] > A[j]:
            ci += 1
            A[j], A[j - 1] = A[j - 1], A[j]
            ci += 1
            j -= 1
        i += 1
    return A, ci

def selection_sort(A): # yellow
    cs = 0
    for i in range(len(A) - 1):
        min = i
        cs += 1
        for j in range(i + 1, len(A)):
            if (A[min] > A[j]):
                min = j
            cs += 1
            
        if min != i:
            A[min], A[i] = A[i], A[min]
            cs += 1
        cs += 1

    return A, cs

num_elements = np.arange(10, 101, 10)
print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)
comparacionescb = np.zeros(size)
comparacionesci = np.zeros(size)
comparacionescs = np.zeros(size)
for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) # se crea el vector a ordenar
    # acá se hace una copia de ese vector, para preservar el vector con números aleatorios.
    vector_ord = vector.copy()
    # acá viene la estructura para tomar el tiempo
    t_inicio = perf_counter_ns()
    A, cb = bubble_sort(vector_ord) # se ejecuta el método burbuja con el vector copia
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio # se guarda el tiempo para n elementos, para crear una gráfica.
    comparacionescb[i] = cb
    print(f"Vector ordenado: \n{A}")
    vector_ord = vector.copy() # volvemos a copiar el vector aleatorio original sobre el vector copia para
    # que el siguiente método trabaje sobre los mismos datos
    print(f"Vector sin ordenar: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    A, ci = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio
    comparacionesci[i] = ci
    print(A)
    vector_ord = vector.copy()
    t_inicio = perf_counter_ns()
    A, cs = selection_sort(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio
    comparacionescs[i] = cs
    print(A)

if com == 1:
    plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-", num_elements, t_selection, "y-")
else:
     plt.plot(num_elements, comparacionescb, "g-", num_elements, comparacionesci, "b-", num_elements, comparacionescs, "y-")

plt.show()