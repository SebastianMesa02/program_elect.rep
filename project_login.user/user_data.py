import re #Para caracteres regulares

# Se definen los grupos de caracteres que se admitiran en el correo
signos = ['.', '_', '-']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dominios = ['gmail', 'hotmail', 'live']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = []
extenciones = ['com', 'cl', 'es', 'ru']

# El ciclo sirve para que cada caracter en minusculas pase a mayusculas con la funcion .append(x.upper())
for x in minusculas:
    mayusculas.append(x.upper())

#Definimos la funcion de la clave
def validar_password():
    clave = input('Escriba la contraseña: ') # Se pide la clave
    if 8 <= len(clave) <= 16: # Se evalua si la clave tiene mas de 8 caracteres
        if re.search('[a-z]', clave) and re.search('[A-Z]', clave): # Se evalua si la clave tiene minusculas y mayusculas
            if re.search('[0-9]', clave): # Se valida s la clave tiene numeros
                if re.search('[$@#]', clave): # Se valida si la clave tiene caracteres especiales
                   print("Sesion iniciada") # Tal caso inicia sesion porque es una clave valida
    else:
        print("Contraseña incorrecta") # De lo contrario la contraseña es incorrecta

# Definimos la funcion para el usuario
def user(signos, numeros, dominios, minusculas, mayusculas, extenciones): #Se incluyen los grupos de caracteres definidos
    email = input("Escribe tu correo") # Pedimos el usuario
    problema = "" #Inicializamos una variable donde guadaremos el resultado

    if "@" in email: #Se busca @ en el string
        nuevo_email = email.split('@') #Si  hay el @ entonces con la funcion .split se divide el string desde ese espacio
        usuario = nuevo_email[0] #Llamamos a la primero parte el usuario
        resto = nuevo_email[1]
        continuacion = resto.split('.') #Al resto tambien lo dividimos donde haya un . porque existe el dominio y la terminacion del correo ex. gmail.com
        dominio = continuacion[0]
        terminacion = continuacion[1]

        for x in usuario: #Se recorre el usuario
            if x in signos or x in numeros or x in minusculas or x in mayusculas: #Se valida que los caracteres en el correspondan al grupo de numeros, signos, mayusculas y minusculas para que sea un correo valido
                if dominio in dominios: #Se valida que el string dominio esté en el grupo dominios
                    if terminacion in extenciones: #Igual con terminacion en extenciones
                        problema = "el correo es correcto " #Se valida correctamente
                        validar_password() #Por ende se llama a la funcion password
                        break
                    else:
                        problema += "la terminacion no es comun" #Si terminacion no está en extensiones
                else:
                    problema += "el dominio no es reconocido" #Si dominio no está en dominios
            else:
                problema += "el valor" + x + "no es valido para un correo" #Si no tiene mayus, minus, signo o numeros

    else:
        problema += "el correo no tiene un arroba" #Si no tiene @

    print(problema) #Imprime lo guardado en la variable

user(signos, numeros, dominios, minusculas, mayusculas, extenciones) #se inicia la funcion

