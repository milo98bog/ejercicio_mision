# Hacer un programa que pida al usuario las tres notas de un alumno 
# (deben estar entre 0 y 5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje 
# si aprobó o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro del
# rango permitido.

suma = 0 # lugar donde se almacena y suma las notas ingresadas
i = 3 # Numero de notas que el programa pide ingresar
while (i > 0):
    print("ingrese la nota numero",i)
    nota = input()
    nota = float(nota) # se convierte la entrada en formato decimal 
    if nota>=0 and nota<=5: # se verifica que este entre 0 y 5 
        suma = suma + nota
        i-=1
        promedio = suma/3 # se obtine el promedio de las notas ingresadas
        if promedio >=3:
            respuesta = ("felicidades aprobo la materia")# se verifica que la nota sea mayor de tres para aprobar
        if promedio <3:
           respuesta = ("lo lamento no logro aprobar la materia")
              
print("el promedio es",promedio,respuesta)
    
