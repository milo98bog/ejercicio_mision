def mayo_de_edad(nombre:str, edad:int):
    if not isinstance(nombre,str) or nombre == None:
       return "debe ingresar su nombre en texto"
    if not isinstance(edad,int) or edad == None:
       return "debe ingresar su edad sin puntos ni texto"
    if edad < 1 or edad > 150:
       return "La edad debe estar entre 1 año hasta 150 años"
    if edad >= 18:
        mensaje = "Es usted mayor de edad"
    else:
        mensaje = "Usted aun no cumple con la mayoria de edad"
    
    return f"su nombre es {nombre} su edad es {edad} y {mensaje} "

print(mayo_de_edad("santiago",23))