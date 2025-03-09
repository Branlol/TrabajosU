print("Bienvenido a la mini calculadora!!!!")
salir = False
opesal = False
print("Para realizar alguna operacion aritmetica lo unico que tienes que hacer es escribir el numero que acompaña la operacion.")
while salir == False:
    while opesal == False:
        Operacion = int(input("Lista de operaciones \n1.Suma \n2.Resta \n3.Multiplicacion \n4.Division: \n"))
        if Operacion > 0 and Operacion < 5: 
            if Operacion == 1:
                Opp = "Sumar"
                N1 = int(input(f"Por favor escribe el primer valor que deseas {Opp}\n"))
                N2 = int(input("Ahora escribe el 2do valor:\n"))
                Resultado = N1 + N2
            elif Operacion == 2:
                N1 = int(input(f"Por favor escribe el primer valor:\n"))
                N2 = int(input("Ahora escribe el 2do valor:\n"))
                Resultado = N1 - N2
            elif Operacion == 3:
                Opp = "Multiplicar"
                N1 = int(input(f"Por favor escribe el primer valor que deseas {Opp}\n"))
                N2 = int(input("Ahora escribe el 2do valor:\n"))
                Resultado = N1 * N2
            elif Operacion == 4:
                N1 = int(input(f"Por favor escribe el numerador de la division:\n"))
                N2 = int(input("Ahora escribe el denominador:\n"))
                Resultado = N1 / N2
        print(f"El resultado es {Resultado}")
        Fuera = input("Si deseas realizar otro ejercicio escribe cualquier cosa, si no deseas realizar mas ejercicios "
        "escribe salir de la siguiente manera: SALIR\n")
        if Fuera == "SALIR":
            salir = True
        else:
            print("Bienvenido de nuevo")
                
                

