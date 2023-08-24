palabra = input("Ingresa una palabra: ")
if palabra[::-1]==palabra:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")