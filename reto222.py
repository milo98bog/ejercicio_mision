informacion={

    "id_cliente":1,
    "nombre": "Johana Fernandez ", 
    "edad":20,
    "primer_ingreso": True
}

def cliente (informacion: dict):

    atraccion={
        "X-Treme":20000,
        "Carros chocones":5000,
        "Sillas voladoras":10000
    }

    if informacion["edad"]>18:
        
        informacion["apto"]=True
        informacion["atraccion"]="X-Treme"

        if informacion ["primer_ingreso"]==False:
            informacion ["total_boleta"]=20000

        else:
            informacion ["total_boleta"]=20000 - (20000*5/100)

            
    elif informacion["edad"]>=15 and informacion["edad"]<=18:
        
        informacion["apto"]=True
        informacion["atraccion"]="Carros chocones"

        if informacion ["primer_ingreso"]==False:
            informacion ["total_boleta"]=5000

        else:
            informacion ["total_boleta"]=5000 - (5000*7/100)  

    elif informacion["edad"]>=7 and informacion["edad"]<=15:
        
        informacion["apto"]=True
        informacion["atraccion"]="Sillas voladoras"

        if informacion ["primer_ingreso"]==False:
            informacion ["total_boleta"]=10000

        else:
            informacion ["total_boleta"]=10000 - (10000*7/100)

    else: 
        informacion["atraccion"]="N/A"  
        informacion["apto"]=False
        informacion ["total_boleta"]="N/A"
               

    return {'nombre': informacion ['nombre'], 'edad': informacion ['edad'], 'atraccion': informacion  ['atraccion'], 'apto': informacion ['apto'] ,'primer_ingreso': informacion ['primer_ingreso'], 'total_boleta': informacion ['total_boleta'],}

print (cliente(informacion))