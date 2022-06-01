# Crear un algoritmo que permita saber si una ecuación cuadrática tiene o no solución.
# Recuerde que una ecuación cuadrática se define como:
# x =-b +- ** b**2 - 4ac / 2a
# Y se dice que tiene solución si el valor del discriminaste (que corresponde al cálculo
# interno de la raíz cuadrada b**2−4ac) es mayor o igual a cero y el valor de a es diferente de cero.

from tkinter import N


def ecuacion_cuadratica(a:float,b:float,c:float):
    a = float(a)
    b = float(b)
    c = float(c)
    
    if a != 0:
        respuesta = f"El valor de a es diferente a cero"
        # verificamos que a sea diferente a cero
        operacion = (b**2-4*(a*c))
        # se realiza la operación matematica para determinar que el valor discriminante sea mayor o igual a cero
        
        if operacion >= 0:
            respuesta_disciminante = f"El valor discriminante es {operacion} y por lo tanto la operación tiene solución"
        else:
            respuesta_disciminante = f"El valor discrimante es {operacion} y por lo tanto no tiene solucion "
    else:
        respuesta = f"El valor de a no es diferente a cero por ello la ecuacion cuadratica no tiene solución"
     
    return f"{respuesta}\n{respuesta_disciminante}"

print(ecuacion_cuadratica(2,8,2))