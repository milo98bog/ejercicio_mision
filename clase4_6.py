#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
#la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado 
#redondeado con dos decimales.

def indice_de_masa_corporal(peso_kg:float,altura_m:float):
    if peso_kg > 0 and  altura_m >0:
    #verificamos que se ingrese valores positivos en ambas entradas
        imc = round(peso_kg/altura_m**2,2)
    #se realiza el calculo del indice de masa corporal
        respuesta = f"Su indice de masa corporal es {imc}"
    else:
        respuesta = f"Debe ingresar un valores positivos "
    
    return respuesta

print(indice_de_masa_corporal(68.5,1.65))