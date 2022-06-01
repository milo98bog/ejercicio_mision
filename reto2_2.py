informacion = {
    'id_cliente': 1,
    'nombre':'Johana Fernandez',
    'edad': 20,
    'primer_ingreso': True,
}


def cliente (informacion:dict)-> dict:

    if informacion ['edad'] >=7:
        apto = True 
    else: 
        apto = False 
    
    if informacion ['edad'] > 18: 
        juego = 'X-Treme'
        if informacion ['primer_ingreso'] == True:
            descuento_boleta = (20000-((20000*5)/100))
        else:
            descuento_boleta = 20000
    elif informacion ['edad'] >=15 and informacion ['edad']<= 18: 
        juego = 'Carros chocones'
        if informacion ['primer_ingreso'] == True:
            descuento_boleta= (5000-((5000*7)/100))
        else:
            descuento_boleta = 5000
    elif informacion ['edad'] >= 7 and informacion ['edad'] < 15:
        juego = 'Sillas voladoras'
        if informacion ['primer_ingreso'] == True:
            descuento_boleta = (10000-((10000*5)/100))
        else:
            descuento_boleta = 10000
    else:  
        descuento_boleta = 'N/A'
        juego = 'N/A'
            
    return {'nombre':informacion['nombre'] , 'edad':informacion['edad'] , 'atraccion': juego ,'apto': apto , 'primer_ingreso': informacion['primer_ingreso'], 'total_boleta': descuento_boleta}

print(cliente(informacion))