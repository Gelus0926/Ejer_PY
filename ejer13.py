#Construir un programa que reciba el tamaño de una lista
#y la llene con numeros entregados por el usuario
lista=[]
cantidad=int(input("Ingrese el tamaño de la lista:"))

for x in range(cantidad):

    valor=int(input("Ingrese un valor entero:"))
    lista.append(valor)

print(lista)