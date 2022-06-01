# Crea un programa que dado un número entero que designa un periodo de tiempo expresado en segundos,
# imprima el equivalente en días, horas, minutos y segundos.

def equivalente(segundos:int):
    segundos = int(segundos)
    if segundos>0:
        dias = segundos //(24*60*60)
        segundos = segundos %(24*60*60)
        horas = segundos //(60*60)
        segundos = segundos%(60*60)
        minutos = segundos// 60
        segundos = segundos%60
        
        respuesta=f"dias {dias} horas {horas} minutos {minutos} segundos {segundos}"
    else:
        respuesta="Debe ingresar un numero positivo mayor a cero"
        
    return respuesta
print(equivalente(7400))


