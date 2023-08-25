def palindromo(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")

    return palabra == palabra[::-1]

def main():
    palabra = input("Ingresa una frase: ")
    
    if palindromo(palabra):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()