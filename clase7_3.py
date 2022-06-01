# Hacer un algoritmo que calcule el total a pagar por la compra de camisas. 
# Si se compran tres camisas o más se aplica un descuento del 20% sobre el total 
# de la compra y si son menos de tres camisas un descuento del 10%


valor_camisetas = 0.0
total_pagar = 0
contar_unidades = 0
mensaje = "Introduzca la nota de un estudiante (0 para salir):"

precio_camiseta = int(input(mensaje))

while precio_camiseta != 0:
    total_pagar = total_pagar + precio_camiseta
    contar_unidades = contar_unidades + 1
    precio_camiseta = int(input(mensaje))
    
if contar_unidades>=3:
    descuento_veinte = total_pagar*20/100
    descuento_veinte = total_pagar - descuento_veinte
    respuesta = ("el descuento es del 20 ",descuento_veinte)
    
else:
     descuento_diez = total_pagar*10/100
     descuento_diez = total_pagar - descuento_diez
     respuesta = ("el descuento del 10",descuento_diez)
    
print("el total a pagar es:", respuesta)