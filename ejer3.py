#3.Recibir dos numeros y determinar cual es mayor
print("Ingrese dos numeros:")
n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
 
if n1==n2:
    print("Los dos numeros son iguales")
elif n1>n2:
    print(f"El numero {n1} es mayor que {n2}")
else:
    print(f"El numero {n2} es mayor que {n1}")
 
