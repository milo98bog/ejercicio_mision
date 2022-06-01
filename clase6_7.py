def imprimir_mensaje(letra:str):
    letra = letra.upper()
    if letra == "A":
        return f"{letra} Android" 
    elif letra == "I":
        return f"{letra} IOS" 
    else:
        return f"{letra} opción invalida"

print(imprimir_mensaje("c"))