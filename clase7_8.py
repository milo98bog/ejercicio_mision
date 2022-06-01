# Crear un algoritmo que indique el valor del descuento de un artículo dependiendo de su valor:
# Rango de valores	Descuento
# $ 0 hasta $100.000 -- 0%
# mas de $100.000 hasta $225.000 -- 1.5%
# mas de $225.000 hasta $375.000 -- 3.8%
# mas de $375.000 -- 1.5%

def descuento_producto(valor_producto:float):
    
    if valor_producto>0  and valor_producto<=100000:#si el numero es menor de 100 mil
        respuesta = f"el descuento es de 0%, y el valor a pagar es de {valor_producto}"
        
    elif valor_producto>100000  and valor_producto<=225000:# el numero es mayor de 100 mil y menor o igual a 275mil
        descuento_producto = round(valor_producto*1.5/100,1)
        valor_total = round(valor_producto - descuento_producto,1)
        respuesta = f"el descuento es de 1.5% {descuento_producto} y el valor total a pagar es {valor_total}"
        
    elif valor_producto>225000  and valor_producto<=375000:# el numero es mayor de 225 mil y menor o igual a 375mil
        descuento_producto = round(valor_producto*3.8/100,1)
        valor_total = round(valor_producto - descuento_producto,1)
        respuesta = f"el descuento es de 3.8% {descuento_producto} y el valor total a pagar es {valor_total}"
    
    elif valor_producto>375000:# el numero es mayor de 375 mil
        descuento_producto = round(valor_producto*1.5/100,1)
        valor_total = round(valor_producto - descuento_producto,1)
        respuesta = f"el descuento es de 1.5% {descuento_producto} y el valor total a pagar es {valor_total}"
    else:
        respuesta = f"el numero debe ser positivo y mayor a cero"

    
        
    return respuesta

print(descuento_producto(1))