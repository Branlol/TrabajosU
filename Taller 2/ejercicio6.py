def evaluar_polinomio(coeficientes, x):
    """Evalúa un polinomio dado por sus coeficientes en un punto x"""
    resultado = 0
    grado = len(coeficientes) - 1
    for i in range(len(coeficientes)):
        resultado += coeficientes[i] * (x ** (grado - i))
    return resultado

def calcular_area(coeficientes, n_rectangulos):
    """Calcula el área bajo la curva usando suma de Riemann izquierda"""
    area = 0.0
    base = 1 / n_rectangulos
    for i in range(n_rectangulos):
        x = i * base
        altura = evaluar_polinomio(coeficientes, x)
        # Recortar altura fuera del terreno
        if altura < 0:
            altura = 0
        elif altura > 1:
            altura = 1
        area += base * altura
    return area

# Lógica principal
while True:
    grado = int(input())
    if grado == 20:
        break

    coeficientes = list(map(int, input().split()))
    n = int(input())

    area_cain = calcular_area(coeficientes, n)
    area_abel = 1 - area_cain
    diferencia = abs(area_cain - area_abel)

    if diferencia <= 0.001:
        print("JUSTO")
    elif area_cain > area_abel:
        print("CAIN")
    else:
        print("ABEL")