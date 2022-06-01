
def nota_definitiva(nota:float):
   
    if not isinstance(nota,float) or nota == None:
       return "debe ingresar un valor decimal"
    if nota < 0.0 or nota > 5.0:
        return "Las notas definitivas deben estar entre 0.0 y 5.0"
    if nota >= 4.0:
        mensaje = "felicitaciones"
    else:
        mensaje = ""
    
    return f"su nota final es {nota} {mensaje} "
     



print(nota_definitiva(5))