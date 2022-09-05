#Construir un programa que reciba el tamaño de una lista
#y la llene con multiplos de 7
lista=[]
cantidad=int(input(f"Ingrese el tamaño de la lista:"))
contador=1


for cont in range(cantidad):

    valor=contador * 7
    lista.append(valor)
    contador+=1

print(lista)