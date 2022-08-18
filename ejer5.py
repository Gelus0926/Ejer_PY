#5.Una compañia de software contable,paga a su personal de ventas
#un salario de 3500000 mensuales, mas una comisión de 1500000
#por cada licencia de software vendida menos el
#(5% del salario total + comisiones de deducciones)por impuestos.
#Codifica un programa que calcule e imprima el salario mensual
#de un vendedor dado recibiendo el numero de ventas realizadas.
 
def calculo (x = input("La cantidad de licencia vendidas son: ")) :
 
    licencia = int(x)
    salario = int(3500000)
    comision = int(1500000)
    total = int(((comision + salario) * 0.05)* licencia)
    totalsalario = total + salario
    resultado = print(f'El salario mensual de un vendedor es {totalsalario}')
    return resultado
 
print(calculo())
