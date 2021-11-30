# Menu de Opciones
#   Seleccionar entre diferentes operaciones; Suma, resta, multiplicacion y division
#   Controlar division entre 0


print("Este programa es una calculadora ")

# Imprimimos el menú en pantalla
print("""
                1) Suma       3) Multiplicacion
                2) Resta      4) Division
                """)

# Se lee la entrada
opcion = input("Selecciona una opcion: ")

# Codigo para suma
if opcion == "1":
    print("\n Suma \n")
    print("Ingrese el primer numero: ")
    firstNumber = float(input())
    print("Ingrese el segundo numero: ")
    secondNumber = float(input())

    sum_numbers = firstNumber + secondNumber
    print("El resultado es: ", sum_numbers)

# Codigo para resta
elif opcion == "2":
    print("\n Resta \n")
    print("Ingrese el primer numero: ")
    firstNumber = float(input())
    print("Ingrese el segundo numero: ")
    secondNumber = float(input())

    res_numbers = firstNumber - secondNumber
    print("El resultado es: ", res_numbers)

# Codigo para multiplicacion
elif opcion == "3":
    print("\n Multiplicacion \n")
    print("Ingrese el primer numero: ")
    firstNumber = float(input())
    print("Ingrese el segundo numero: ")
    secondNumber = float(input())

    mul_numbers = firstNumber * secondNumber
    print("El resultado es: ", mul_numbers)

# Codigo para division con validacion de entrada = 0
elif opcion == "4":
    print("\n Division \n")
    print("Ingrese el primer numero: ")
    firstNumber = float(input())
    print("Ingrese el segundo numero: ")
    secondNumber = float(input())
    if firstNumber == 0:
        print("Division en 0 no realizada, intente con otro valor")
    elif secondNumber == 0:
        print("Division en 0 no realizada, intente con otro valor")
    else:
        div_numbers = (firstNumber) / (secondNumber)
        print("El resultado es: ", div_numbers)

# Caso de entrada incorrecta
else:
    print("Opción no válida")