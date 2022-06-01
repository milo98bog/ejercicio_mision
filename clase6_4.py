def numero_par_impar(numero:int):
       
    if not isinstance(numero,int) or numero == None:
       return "debe ingresar un valor entero"
    if numero % 2 ==0:
        mensaje = "El numero es par"
    else:
        mensaje = "El numero es impar"
    
    return f"el numero {numero} es {mensaje} "

print(numero_par_impar(500))