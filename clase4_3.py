
def multiplica(valor_factura:int, valor_iva = 19):

#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
# devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 19%.

  if valor_factura > 0: 
    
    if  type(valor_iva) == int :
        a = (valor_factura*valor_iva/100)
        a = (a+valor_factura)
    else:
          a ="error maracas"  
  else:
    a = "error"
      
  return a

print(multiplica(1000,"hola"))