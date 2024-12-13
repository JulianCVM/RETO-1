#Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, 
# minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud 
# y las preferencias del usuario y devuelve una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas 
# y permite al usuario realizar múltiples solicitudes.
#Instrucciones:
#Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
#Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
#Utilizará una función para generar la contraseña según las preferencias del usuario.
#Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
#Si el usuario decide salir, se despedirá y el programa se cerrará.
#
#Se debe entregar el/los archivos de Python o el indicado por el Trainer, en el cual contenga el código del programa en cuestión.


import random

isMayus = True
isMinus = True
isCaract = True
isSimbols = True

contraseña = ""

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]



#longitud=int(input("asdº  "))

def generar_contra(longitud):
    if longitud==4:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            palabra1 = abc[i]
            palabra2 = abc[i+longitud]
            palabra3 = abc[i-longitud]
            palabra4 = abc[i//longitud]
        contraseña = [palabra1+palabra2+palabra3+palabra4]
        return contraseña
    elif longitud==5:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i*2]
            palabra2 = abc[i-longitud]
            palabra3 = abc[i+longitud]
            palabra4 = abc[i//longitud-1]
            palabra5 = abc[i//longitud+1]
        contraseña = [palabra2+palabra1+palabra4+palabra5+palabra3]
        return contraseña
    elif longitud==6:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i+5]
            palabra2 = abc[i+longitud-2]
            palabra3 = abc[i+longitud//2]
            palabra4 = abc[i//longitud+4]
            palabra5 = abc[i//longitud-3]
            palabra6 = abc[i%longitud+1-2]
        contraseña = [palabra3+palabra1+palabra5+palabra6+palabra4+palabra2]
        return contraseña
    elif longitud==7:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i+7]
            palabra2 = abc[i-longitud-1]
            palabra3 = abc[i-longitud+7]
            palabra4 = abc[i//longitud+i//2]
            palabra5 = abc[i+longitud+3]
            palabra6 = abc[i%longitud+4]
            palabra7 = abc[i+3*2]
        contraseña = [palabra7+palabra6+palabra1+palabra2+palabra5+palabra3+palabra4]
        return contraseña
    elif longitud==8:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i-1]
            palabra2 = abc[i+longitud-2]
            palabra3 = abc[i+longitud-5]
            palabra4 = abc[i//longitud+6]
            palabra5 = abc[i//longitud+9]
            palabra6 = abc[i+longitud+1]
            palabra7 = abc[i+longitud-3]
            palabra8 = abc[i-longitud-5]
        contraseña = [palabra2+palabra4+palabra6+palabra8+palabra1+palabra3+palabra5+palabra7]
        return contraseña
    elif longitud==9:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i-10]
            palabra2 = abc[i+longitud-10]
            palabra3 = abc[i-longitud+4]
            palabra4 = abc[i-longitud-2]
            palabra5 = abc[i-longitud+7]
            palabra6 = abc[i-longitud+9]
            palabra7 = abc[i-longitud+13]
            palabra8 = abc[i-longitud+3]
            palabra9 = abc[i-longitud-2]
        contraseña = [palabra1+palabra3+palabra5+palabra7+palabra9+palabra2+palabra4+palabra6+palabra8]
        return contraseña
    elif longitud==10:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i-5]
            palabra2 = abc[i//longitud-1]
            palabra3 = abc[i//longitud+1]
            palabra4 = abc[i//longitud-2]
            palabra5 = abc[i//longitud+2]
            palabra6 = abc[i//longitud-3]
            palabra7 = abc[i//longitud+3]
            palabra8 = abc[i//longitud+4]
            palabra9 = abc[i//longitud-4]
            palabra10 = abc[i//longitud+5]
        contraseña = [palabra10+palabra9+palabra8+palabra7+palabra6+palabra1+palabra2+palabra3+palabra4+palabra5]
        return contraseña
    elif longitud==11:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i%longitud-2]
            palabra2 = abc[i%longitud+2]
            palabra3 = abc[i%longitud-3]
            palabra4 = abc[i%longitud+4]
            palabra5 = abc[i%longitud+5]
            palabra6 = abc[i%longitud+6]
            palabra7 = abc[i%longitud-7]
            palabra8 = abc[i%longitud-8]
            palabra9 = abc[i%longitud-9]
            palabra10 = abc[i%longitud-10]
            palabra11 = abc[i%longitud]
        contraseña = [palabra1+palabra4+palabra8+palabra2+palabra6+palabra7+palabra9+palabra3+palabra5+palabra11+palabra10]
        return contraseña
    elif longitud==12:
        for i in range(longitud):
            abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r"]
            palabra1 = abc[i-i+2]
            palabra2 = abc[i-i]
            palabra3 = abc[i-longitud]
            palabra4 = abc[i+longitud-10]
            palabra5 = abc[i//longitud+2]
            palabra6 = abc[i%longitud-1]
            palabra7 = abc[i//longitud-3]
            palabra8 = abc[i+longitud-23]
            palabra9 = abc[i-longitud-1]
            palabra10 = abc[i%longitud-1]
            palabra11 = abc[i+i-5]
            palabra12 = abc[i-5+1]
        contraseña = [palabra5+palabra10+palabra12+palabra1+palabra6+palabra11+palabra3+palabra7+palabra9+palabra2+palabra4+palabra8]
        return contraseña
         

on = True
while on:
    print("Bienvenido usuario\nEste programa es un generador de contraseñas seguras el cual le va a proporcionar su contraseña de acceso segura según lo que usted desee\nPara ello necesitamos que nos indique los siguientes parametros a tener en cuenta:")
    longitud = int(input("Ingrese la longitud de la contraseña (maximo 12 caracteres, minimo 4): "))
    #mayus = int(input("Desea incluir mayusculas? \n1)Si \n2)1No"))
    #minus = int(input("Desea incluir minusculas? \n1)Si \n2)1No"))
    #caract = int(input("Desea incluir mayusculas? \n1)Si \n2)1No"))
    #simbols= int(input("Desea incluir mayusculas? \n1)Si \n2)1No"))
    
    if(longitud>=4 and longitud<=12):
        print(generar_contra(longitud=longitud))
        break
    else:
        print("Ingrese un rango valido para generar la contraseña")

