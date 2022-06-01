#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos
#y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

def empaque_paquetes(payasos:int,muñecas:int):
    cantidad_payasos = int(payasos)
    cantidad_muñecas = int(muñecas)
    # se convierte las entradas en valores enteros
    if cantidad_payasos >= 0 and cantidad_muñecas >=0:
    # se veridfica que sea un numero positivo
        carga_payasos = cantidad_payasos*112
        carga_muñecas = cantidad_muñecas*75
    # se realiza operaciones matematicas para definir el valor en gramos de la carga a transportar
        total_carga = carga_payasos + carga_muñecas
        respuesta = f"el total de la carga en gramos es {total_carga} , donde el peso en gramos de los payasos es {carga_payasos} y el peso en gramos de las muñecas es {carga_muñecas}"
    else:
        respuesta = f"se debe ingresar un valor positivo en las dos entradas "
    return respuesta

print(empaque_paquetes(0,3))