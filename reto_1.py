
def CDT(usuario:str, capital:int, tiempo:int):
    
    if tiempo > 2:
        valor_intereses = (capital*3/100*tiempo)/12
        valor_total = (valor_intereses+capital)
       
    else:
        valor_perder = capital*2/100
        valor_total = capital-valor_perder
    
    retorno = f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
    return retorno
    
print(CDT("camilo",100000,3))
	  
     
     
