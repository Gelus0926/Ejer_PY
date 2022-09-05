#Leer 20 numeros enteros y guardar en una lista,
#despues permitir que el usuario busque un numero
#y si este se encuentra en la lista indicar
#con un mensaje que el resultado es exitoso
lista=[]
contador=1


for cont in range(5):

    valor=int(input(f"Digite numeros: "))
    lista.append(valor)
    contador+=1

numeroBuscado=int(input(f"numero por encontrar: "))

encontro=''
for num in lista:
    if num==numeroBuscado:
        
        encontro='encontro'
        break

if encontro=='encontro':
    print(f'el resultado fue exitoso {numeroBuscado}')
else:
    print(f'el numero no ha sido encontrado')






##print(lista)
