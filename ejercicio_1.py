numero = int(input("Ingrese un numero para saber si es primo o no: "))

#bool(1)True
#bool(0)False

def primo(a):
    
    divisores = 0
    
    for a in range(1, numero+1):
    
        if numero % a == 0:
            divisores = divisores + 1
            
    return divisores
    

if primo(numero) == 2:
    print(bool(1))
else:
    print(bool(0))