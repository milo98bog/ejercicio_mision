# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
# del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace
# por no ser fresca y el coste final total.
def pan_del_dia(numero_de_panes:int):
    numero_de_panes = int(numero_de_panes)
# lee el valor ingresado y lo convierte a entero
    if numero_de_panes>0:
# verifica que el numero sea positivo y mayor a cero
        valor_pan = 3.94
        porcentaje = valor_pan*60/100 
        porcentaje_total = valor_pan-porcentaje
# se obtine el valor del descuento por unidad
        valor_descuento = round(porcentaje_total*numero_de_panes,3)
        respuesta = f"El valor habitual de una barra de pan es {valor_pan} y el valor total de {numero_de_panes} piezas con el descuento por no ser fresco es de {valor_descuento}"
    else:
        respuesta = f" Debe ingresar un numero positivo y mayor a cero "
    return respuesta
    
print(pan_del_dia(1))