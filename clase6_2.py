def nota_definitiva(nota:float):
       
    if not isinstance(nota,float) or nota == None:
       return "debe ingresar un valor decimal"
    if nota < 0.0 or nota > 5.0:
        return "Las notas definitivas deben estar entre 0.0 y 5.0"
    if nota >= 3.0:
        mensaje = "felicidades aprobo el curso"
    else:
        mensaje = "lamentable mente reprobo el curso"
    
    return f"su nota final es {nota} {mensaje} "

print(nota_definitiva(2.0))