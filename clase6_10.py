def recibo_de_agua(estrato:int,metro_consumido:int):
    if estrato == 1:
        cargo = 2500
        valor_metro = 2200
        basura_alcantarillado = 5500
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
       
    elif estrato == 2:
        cargo = 2800
        valor_metro = 2350
        basura_alcantarillado = 6200
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
    
    elif estrato == 3:
        cargo = 3000
        valor_metro = 2600
        basura_alcantarillado = 7400
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
       
    
    elif estrato == 4:
        cargo = 3300
        valor_metro = 3400
        basura_alcantarillado = 8600
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
       
    elif estrato == 5:
        cargo = 3700
        valor_metro = 3900
        basura_alcantarillado = 9700
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
    
    elif estrato == 6:
        cargo = 4400
        valor_metro = 4800
        basura_alcantarillado = 11000
        total = cargo + valor_metro*metro_consumido + basura_alcantarillado 
    
    retro = f"su estrato es {estrato} y su valor a pagar es {total}" 
    return retro
    
    
print(recibo_de_agua(6,5))