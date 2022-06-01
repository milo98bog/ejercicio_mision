def numero_mayor (num_1:float,num_2:float,num_3:float,num_4:float):
    a = [num_1,num_2,num_3,num_4] # convertimos los valores de la funcion en una lista
    milo = max(a)# usando la funcion max() maximo busacmor el valor maximo en la lista 
    return f"El numero mayor es {milo} "# devolvemos el valor maximo que se encontro en la lista 

print(numero_mayor(300,2000,3,4))