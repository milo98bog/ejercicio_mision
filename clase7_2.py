# A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora.
# Si la cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% 
# para las horas extras. Calcular el salario del trabajador dadas las horas trabajadas 
# y la tarifa ingresadas por el usuario.

def horas_trabajadas(horas:int):
    horas = int(horas)
#convertimos el valor ingresado a entero
    valor_hora = 4000
    if horas>0: 
#verificamos que sea un numero positivo mayor a cero
        if horas >40 :
            horas_extra = horas - 40
#verificamos cuantas horas extra trabajo despues de la hora 40
            tarifa_extra = valor_hora*50/100
            total_extra = horas_extra * tarifa_extra
#agregamos el valor ganado por el incremento en la hora trabajada
            valor_sueldo = horas*valor_hora
            total_sueldo = valor_sueldo + total_extra
#asignamos el valor a pagar por hora trabajada
            respuesta = f"el valor total del sueldo con el incremento por acumuar mas de 40 horas de trabajo es {total_sueldo}"
        else:
            total_sueldo = horas*valor_hora
        respuesta = f"el valor total del sueldo sin incremento es {total_sueldo}"
    else:
        respuesta ="el numero debe ser positivo y mayor a cero"

    
        
    return respuesta

print(horas_trabajadas(41))