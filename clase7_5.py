# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el 
# usuario lo introduzca muestre por pantalla "<NOMBRE> tiene <n> letras", donde <NOMBRE> es
# el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

def mayuscula(nombre:str):
    nombre =str(nombre)
    nombre = nombre.upper()
    apodo = len(nombre)
    print("el nombre tiene",apodo,"letras")
    return nombre

print("Hola!!! cual es tu nombre")
nombre = input()
print(mayuscula(nombre))