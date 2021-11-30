def menu():
    print("\n Este programa es una calculadora \n")
    print("""
                    1) Suma       3) Multiplicacion
                    2) Resta      4) Division
                    """)


menu()


def menuValue():
    return int(input("Ingrese una opcion del menu: "))


menuOption = menuValue()


def sumNumber(firstNum, secondNum):
    print("\n Suma \n")
    print("La suma es " + str(firstNum + secondNum))
    return menu(), menuOption


def resNumber(firstNum, secondNum):
    print("\n Resta \n")
    print("La resta es " + str(firstNum - secondNum))


def mulNumber(firstNum, secondNum):
    print("\n Multiplicacion \n")
    print("La multiplicacion es " + str(firstNum * secondNum))


def divNumber(firstNum, secondNum):
    print("\n Division \n")
    if firstNum == 0:
        print("Division en 0 no realizada, intente con otro valor")
    elif secondNum == 0:
        print("Division en 0 no realizada, intente con otro valor")
    else:
        div_numbers = (firstNum) / (secondNum)
        print("El resultado es: ", div_numbers)


firstNum = float(input("Digite el primer valor: "))
secondNum = float(input("Digite el segundo valor: "))

def opMenu(menuOption):
    if menuOption == 1:
        sumNumber(firstNum, secondNum)
    elif menuOption == 2:
        resNumber(firstNum, secondNum)
    elif menuOption == 3:
        mulNumber(firstNum, secondNum)
    elif menuOption == 4:
        divNumber(firstNum, secondNum)
    else:
        print("Opcion no valida")


opMenu(menuOption)
