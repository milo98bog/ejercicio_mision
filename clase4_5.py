#Escribir un programa que lea un entero positivo n, introducido por el usuario 
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta n

def suma_posito(numero:int):
    numero_positivo = int(numero)
    # se convierte el numero ingresado a entero
    if numero_positivo >=1:
    # se verifica que el numero ingresado sea igual o mayor a uno 
        suma_positiva = numero_positivo*(numero_positivo+1)/2
        respuesta = f"el valor es {suma_positiva}"
    else:
        respuesta = f"debe ingresar un numero positivo" 
    return respuesta

print(suma_posito(10))