#Escribir una función que calcule el área de un círculo y 
#otra que calcule el volumen de un cilindro usando la primera función.

from math import*
def area(radio:float,altura:float):
    if altura > 0:
        # si el usuario ungresa un valor mayor a cero en altura definira que 
        # necesita obtener el volumen de un cilindro
        if radio > 0:  
            volumen_cilindro = pi*radio**2*altura
            respuesta = f"el volumen es {volumen_cilindro}"
            
        #la formula del radio es pi*radio**2
        else:
             respuesta = "debe ingresar un valor mayor a 0"
                
    else: 
        # si el usuario ungresa un valor igual o menor a cero en altura definira que 
        # necesita obtener el radio de un circulo 
        if radio > 0:
            radio_circulo = pi * radio**2
            respuesta = f"el radio es {radio_circulo}"
        #la formula del radio es pi*radio**2
        else:
             respuesta = "debe ingresar un valor mayor a 0"
        
    return respuesta

print(area(15.5,-11))