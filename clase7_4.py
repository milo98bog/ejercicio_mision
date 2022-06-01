# Escribir un programa que pregunte el nombre del usuario en la consola y un número 
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido.

def impri_nom(nombre:str,num_veces:int):
    nombre = str(nombre)
    num_veces = int(num_veces)
    
    while num_veces > 0:
        print(nombre)
        num_veces = num_veces - 1
    
    return "gracias "

print('ingresa nombre')
nombre = input()
print('ingresa repeticiones')
num_veces = input()
print(impri_nom(nombre,num_veces))