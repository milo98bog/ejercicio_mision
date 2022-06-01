def incorporacion(genero:str,estatura:float,edad:int,estado:str):
    if genero == "hombre":
        if estatura > 1.65 and edad >=18 and edad <=24 and estado == "soltero":
            respuesta = "El soldado es apto"    
        else:
           respuesta =  "El soldado no es apto"
    
    if genero == "mujer":
        if estatura > 1.60 and edad >=20 and edad <=25 and estado == "soltero":
            respuesta = "El soldado es apto"
            
        else:
           respuesta =  "El soldado no es apto"
    dictamen = f"el resultado del reclutamineto es {respuesta} "
    return dictamen

print(incorporacion("hombre",1.60,20,"soltero"))