# PRIMER PRACTICA

# Python detecta si es string, float, int, etc. es decir, no es necesario poner el tipo de variable

string_var = "Hi teacher" # No es necesario ; 
float_var = 123.45

# Imprime los datos
print(string_var)
print(float_var)

# La funcion type reconoce el tipo de variable es)
print(type(string_var))
print(type(float_var))

# Sumar dos enteros
suma_int = (2+5)
print(suma_int)

# Sumar dos float
num_1 = 3.5
num_2 = 4.8
suma_float = num_1+num_2
print(suma_float)

# Concatenar dos string
string_1 = 'Hola'
string_2 = ' Mundo'
string_res = string_1 + string_2
print(string_res)

import datetime
import sys
# Muestra info del programa y su version
version = sys.version
print(version)

# Muestra de manera desglosada la info de la version
version_info = sys.version_info
print(version_info)

# Muestra fecha actual exacta (aa/mm/dd/hh)
print(datetime.datetime.now())

# Guarda datetime como string y cambia el formato (Dd/Mm/Aa)
current_date = datetime.datetime.now()
print(current_date.strftime("%A %d %B (%m) %y (%Y)"))  # <--- se asigna el formato con % -
print(current_date.strftime("%H:%M:%S"))  # <--- ya que el formato solo especifica datos de tiempo solo se muestra ello

# Condicionales

number = 10
userNumber = int(input("Escriba su entrada: "))

if userNumber == number:
    print("El numero ingresado es igual a ", number)
elif userNumber < number:
    print("El numero ingresado es menor a ", number)
else:
    print("El numero ingresado es mayor a ", number)

