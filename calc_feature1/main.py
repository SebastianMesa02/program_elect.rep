import sys
import time
i = 1
while i >= 1:
    i += 1


    def menu():
        print("\n Este programa es una calculadora \n")
        print("""
                        1) Suma       3) Multiplicacion
                        2) Resta      4) Division
                                5) Salir
                        """)


    menu()

    def menuValue():
        return int(input("Ingrese una opcion del menu: "))


    menuOption = menuValue()


    def sumNumber():
        print("\n Suma \n")
        firstNum = float(input("Digite el primer valor: "))
        secondNum = float(input("Digite el segundo valor: "))
        print("La suma es " + str(firstNum + secondNum))
        time.sleep(3)


    def resNumber():
        print("\n Resta \n")
        firstNum = float(input("Digite el primer valor: "))
        secondNum = float(input("Digite el segundo valor: "))
        print("La resta es " + str(firstNum - secondNum))
        time.sleep(3)


    def mulNumber():
        print("\n Multiplicacion \n")
        firstNum = float(input("Digite el primer valor: "))
        secondNum = float(input("Digite el segundo valor: "))
        print("La multiplicacion es " + str(firstNum * secondNum))
        time.sleep(3)


    def divNumber():
        print("\n Division \n")
        firstNum = float(input("Digite el primer valor: "))
        secondNum = float(input("Digite el segundo valor: "))
        if firstNum == 0:
            print("Division en 0 no realizada, intente con otro valor")
            time.sleep(3)
        elif secondNum == 0:
            print("Division en 0 no realizada, intente con otro valor")
            time.sleep(3)
        else:
            div_numbers = (firstNum) / (secondNum)
            print("El resultado es: ", div_numbers)
            time.sleep(3)




    def opMenu(menuOption):
        if menuOption == 1:
            sumNumber()
        elif menuOption == 2:
            resNumber()
        elif menuOption == 3:
            mulNumber()
        elif menuOption == 4:
            divNumber()
        elif menuOption > 5:
            print("Opcion Invalida")
        elif menuOption == 5:
            print("\n Adios \n")
            sys.exit()


    opMenu(menuOption)
