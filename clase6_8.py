def nota_definitiva(nota:float):
    
    if not isinstance(nota,float) or nota == None: 
        #isinstance() función devuelve True si el objeto especificado es del 
        #tipo especificado, de lo contrario False
        #Si el parámetro de tipo es una tupla, esta función devolverá Truesi el objeto
        # es uno de los tipos de la tupla
       return "debe ingresar un valor decimal"
    if nota < 0.0 or nota > 5.0:
        return "Las notas definitivas deben estar entre 0.0 y 5.0"
    if nota < 3.0:
        return f" {nota} Insuficiente"
    elif nota <= 3.5:
        return f" {nota} aceptable"
    elif nota <= 4.0:
        return f" {nota} sobresaliente"
    elif nota <= 5.0:
        return f" {nota} excenlente"

print(nota_definitiva(4.1))