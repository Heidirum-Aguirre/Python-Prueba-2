palabra = input("Ingrese una palabra a gusto: ")
letrita = input("Eliga la letra que desea contar cuantas veces se repite en su palabra: ")

cont = 0

for letra in palabra:
    if letra == letrita:
        cont =cont + 1
        
print(f"La letra ({letrita}) que usted quiere contar, aparece ({cont}) veces en su palabra ({palabra})")