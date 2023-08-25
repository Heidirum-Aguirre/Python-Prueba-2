opcion = 0

while opcion != 7:
    
    print("Las siguientes opciones de conversion son: ")
    print("1) Kilometros a Milla")
    print("2) Millas a Kilometro")
    print("3) Kilogramos a Libras")
    print("4) Libras a Kilogramos")
    print("5) Celsius a Fahrenheit")
    print("6) Fahrenheit a Celsius")
    print("7) Salir")
    
    opcion = int(input("Ingrese la opcion que deseea de conversion: "))
    numero = int(input("Ingrese el valor a convertir: "))
    resultado = 0
    
    if opcion == 7:
        break
    
    if opcion == 1:
        resultado = (numero * 0.621371)
        
    elif opcion == 2:
        resultado = (numero * 1.60934)
    
    elif opcion == 3:
        resultado = (numero * 2.20462)
        
    elif opcion == 4:
        resultado = (numero * 0.453592)
        
    elif opcion == 5:
        resultado = ((numero * (9/5)) + 32)
        
    elif opcion == 6:
        resultado = ((numero - 32) * (5/9))
        
    else:
        print ("El numero seleccionado no esta dentro de las opciones")
    
    print(f"la conversion del numero ({numero}) es {resultado}")
