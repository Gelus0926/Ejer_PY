#Codificar un programa para que presente un menu de 4 opciones y
#reciba un numero natural para realizar las siguientes operaciones

import math

def m(i):
    if i % 2 == 0:
        print("El numero ",i," es multiplo de 2")
    else:
        print("El numero ",i," no es multiplo de 2")
def r(x):
    y = math.sqrt(x)
    print(y)
def s(x):
    suma= x + 100
    print("si le sumamos 100 el resultado es ",suma,)
def e(x):
    elevar= int(math.pow(x,2))
    print("el numero ingresado elevado a la 2 es: ",elevar,)

num=int(input("ingresar numero: "))


while True:
    print("*** Menu Principal ***")
    print("0 salida")
    print("1.Multiplo del numero ingresado")
    print("2.Raiz cuadrada del numero ingresado")
    print("3.Sumar 100 numeros al numero ingresado")
    print("4.Eleve a la 2 el numero ingresado")
    opc = input("Ingrese una opcion: ")
    if opc=="0":
        break
    elif opc=="1":
        print(m(num))
    elif opc=="2":
        print(r(num))
    elif opc=="3":
        print(s(num))
    elif opc=="4":
        print(e(num))
    else:
        print("Opción invalida")
    
