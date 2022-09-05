""" Construir un programa que reciba numeros enteros y los sume mientras estos
sean positivos, si se digita un numero negativo el programa debe terminar """

#Variable de control
numero =0 

#acumulador
suma=0

#Declaro el ciclo
while numero >= 0:

    #pedir un numero
    numero=int(input("Digite un numero: ")) 

    if numero >= 0 :
        suma=suma+numero
    else:
        print(f'la suma fue: {suma}')
        print(f'Saliendo')
        break

print(f'la suma fue: {suma}')