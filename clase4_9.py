#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
#de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
#la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

def cuenta_ahorros(dinero_ingresado:float):
    
# se transforma el valor ingresado en un entero
    if dinero_ingresado > 0 :
# se verifica que el dinero ingresado y el tiempo trabajado sea positivo y mayor a cero
        porcentaje = dinero_ingresado*4/100
        porncentaje_en_años = porcentaje * 1
# se genera eñ porcentaje de ganacia por un año
        total_recibido1 = round(porncentaje_en_años + dinero_ingresado,2)
        
        total_recibido2 = round(porncentaje_en_años*2 + dinero_ingresado,2)
        
        total_recibido3 = round(porncentaje_en_años*3 + dinero_ingresado,2)
       
        respuesta = f"el valor ganado en el primer años es {total_recibido1} en el segundo año es {total_recibido2} y en el tercer año es {total_recibido3}"
        
    else:
        respuesta = f"El valor en dinero debe ser positivo y mayor a cero"
        
    return respuesta

print(cuenta_ahorros(10000))