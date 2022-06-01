from random import *
def numero_real(numero:float):
    if numero > 3.5 and numero < 7.8:
        return f"el numero {numero} se encuentra dentro del rango"
    else:
        return f"el numero {numero} no se encuentra dentro del rango"

print(numero_real(7.9)) 
 