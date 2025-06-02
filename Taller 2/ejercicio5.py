#5. Construir un programa que reciba las componentes en x y y de un vector y calcule una proyección del 
#mismo sobre un par de vectores unitarios al azar.  El programa de permitir recibir más de un vector, pero uno 
#a la vez. Para cada caso graficar el punto inicial y los puntos que representan las proyecciones



import numpy as np
import matplotlib.pyplot as plt
import random 

# Generar dos vectores unitarios aleatorios
u1 = np.random.rand(2)
u1 = u1 / np.linalg.norm(u1)

u2 = np.random.rand(2)
u2 = u2 / np.linalg.norm(u2)

print("Vector unitario 1:", u1)
print("Vector unitario 2:", u2)

while True:
    print("\nIngrese las componentes del vector (o escriba 'cerrar' para salir)")

    x_input = input("Componente x: ")
    if x_input.lower() == 'cerrar':
        break
    y_input = input("Componente y: ")
    if y_input.lower() == 'cerrar}':
        break

    try:
        x = float(x_input)
        y = float(y_input)
    except:
        print("Entrada inválida, intente otra vez.")
        continue

    v = np.array([x, y])

    # Proyección de v sobre u1
    dot1 = v[0]*u1[0] + v[1]*u1[1]
    p1 = dot1 * u1

    # Proyección de v sobre u2
    dot2 = v[0]*u2[0] + v[1]*u2[1]
    p2 = dot2 * u2

    print("Proyección sobre u1:", p1)
    print("Proyección sobre u2:", p2)

    # Graficar
    plt.figure()
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector original')
    plt.quiver(0, 0, p1[0], p1[1], angles='xy', scale_units='xy', scale=1, color='red', label='Proy. sobre u1')
    plt.quiver(0, 0, p2[0], p2[1], angles='xy', scale_units='xy', scale=1, color='green', label='Proy. sobre u2')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.grid()
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.title("Proyecciones del vector")
    plt.show()