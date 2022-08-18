#4.Juan tiene N cantidad de pesos, Camila tiene la mitad
# de lo que posee Juan y Ricardo tiene la mitad de lo que
# poseen Camila y Juan juntos
# ¿ Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3?
def calculo (x = input("Digite la cantidad de Juan $")) :
 
    juan = int(x)
    c = juan / 2
    camila = int(c)
    r = (camila + juan) / 2
    ricardo = int(r)
    resultado = print(f'Consultando con el sistema Juan tiene : {juan} camila tiene: {camila} y ricardo tiene: {ricardo}')
    return resultado
 
print(calculo())
 
