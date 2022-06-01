print("Ingrese el valor de la computadora escogida")
valor_Pc = float(input())
print("se le recuerda que el descuento por pronto pago es del 10%")
descuento_Prontopago = 10
total = descuento_Prontopago*valor_Pc/100
print("El descuento por pronto pago es", total)
print("El valor total a pagar es ", valor_Pc-total)