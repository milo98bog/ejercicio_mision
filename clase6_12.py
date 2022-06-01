milo = {
    'nom_a':'camilo',
    'nom_b':'ernesto',
    'nom_c':'carlos',
    'capacidad_vaso': 50 ,
}

def gaseosa(cap_1,cap_2,cap_3,cap_llenar,milo:dict):
    
    total_va = milo['capacidad_vaso']-cap_1
    total_vb = milo['capacidad_vaso']-cap_2
    total_vc = milo['capacidad_vaso']-cap_3
    
    if cap_llenar == 10:
        entrega = [total_va-10,total_vb-10,total_vc-10]
        resultado = min(entrega)    
    else:
        entrega = [total_va,total_vb,total_vc]
     
    return resultado
      
   

print(gaseosa(50,10,10,10,milo))