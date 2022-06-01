
informacion={
    "id_cliente":1,
    "nombre": "Johana Fernandez ", 
    "edad":10,
    "primer_ingreso":True,
}

def cliente (informacion:dict):
    
    atraccion={"X-Treme":20000,
    "Carros chocones":5000,
    "Sillas voladoras":10000,
    "juego_1":"X-Treme",
    "juego_2":"Carros chocones",
    "juego_3":"Sillas voladoras"
    }
    if  informacion['edad']>18 and informacion['primer_ingreso'] == True:
        cachaco = atraccion["X-Treme"]*5/100
        total_boleta = atraccion["X-Treme"] - cachaco 
        apto =  informacion['edad']>18 and informacion['primer_ingreso'] == True
        retorno = f"su respuesta es {total_boleta}y es{apto}"
        
    if  (informacion['edad'] >= 15 and informacion['edad'] <= 18) and informacion['primer_ingreso'] == True:
        cachaco = atraccion["Carros chocones"]*7/100
        total_boleta = atraccion["Carros chocones"] - cachaco 
        apto =  (informacion['edad'] >= 15 or informacion['edad'] <= 18) and informacion['primer_ingreso'] == True
        retorno = f"su respuesta es {total_boleta}y es{apto}"
        
    if  (informacion['edad'] > 7 and informacion['edad'] < 15) and informacion['primer_ingreso'] == True:
        cachaco = atraccion["Sillas voladoras"]*5/100
        total_boleta = atraccion["Sillas voladoras"] - cachaco 
        apto =  (informacion['edad'] >= 7 or informacion['edad'] < 15) and informacion['primer_ingreso'] == True
        retorno = f"su respuesta es {total_boleta}y es{apto}"
    
    if informacion['edad']>18 or(informacion['edad'] >= 15 and informacion['edad'] <= 18) or (informacion['edad'] > 7 and informacion['edad'] < 15) and informacion['primer_ingreso'] == False:
        retorno = "falso" 
   
    retorno = f"su respuesta es {total_boleta}y es{apto}"
    return retorno 


print(cliente(informacion))

  
        
    

    