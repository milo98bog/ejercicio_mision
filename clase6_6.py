def numero_real(numero:float):
    if numero > 3.5 and numero <= 7.8 or numero >= 9.5 and numero < 4.5 or numero >= 23.4 and numero <= 45.3  :
        return f"el numero {numero} se encuentra dentro del rango  "
    else:
        return f"el numero {numero} no se encuentra dentro del rango"

print(numero_real(46.6))