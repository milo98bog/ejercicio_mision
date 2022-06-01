#Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.

def numero_par_impar(num_1:int):
    a = num_1> 0 and num_1 < 100
# verificamos que el numero ingresado tenga dos digitos
    if a == True:
        respuesta = "es verdad"
        b = str(num_1)
        c = b[0]
        d = b[1]
        e = int(c)
        f = int(d)
#transformamos los numeros de entero a str los dividivimos y luego los reconvertimos a enteros 
        g = e % 2 ==0
        h = f % 2 ==0
#verificamos si los numeros son pares o impares 
        if g and h:
            seria ="los numeros son pares" 
        elif g == True and h == False:
            seria ="a es par b impar"
        elif g == False and h == True:
            seria ="a es impar b par"
        else:
            seria="a es impar b impar"
    else :
        respuesta = "es mentira"
        seria = "es mentira"
    return respuesta,seria
 

print(numero_par_impar(333))