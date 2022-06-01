# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo
# es el código del país +57, y la extensión tiene dos dígitos (por ejemplo +57-313724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla
# el número de teléfono sin el prefijo y la extensión.

import re
def formato_prefijo(num_telefono:str):
    num_telefono = str(num_telefono)
    respuesta = num_telefono[4:-3]  
    return respuesta

print(formato_prefijo("+57-3014642606-60"))