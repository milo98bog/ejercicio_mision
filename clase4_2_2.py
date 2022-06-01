def factorial(num): 
    if num < 0: 
        print("Factorial de un numero negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = 5; 

print("Factorial de",num,"es", factorial(num)) 
  