#Calcular la estacion segun un mes proporcionado por consola
def estacion_meteorologica(mes):
    if mes.lower() in ('diciembre','enero', 'febrero', 'marzo'):
        return 'Invierno'
    elif mes.lower() in ('marzo','abril','mayo','junio'):
        return 'Verano'
    elif mes.lower() in ('junio','julio','agosto','sepriembre'):
        return 'otoño'
    else:
        return 'primavera'

print("Ingrese un mes del año:")
mes=(input("Mes:"))
print('La estación del año en estos momentos es ' + estacion_meteorologica(mes))