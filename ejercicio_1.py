frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0

for x in frase:
    if x == letra:
        contador += 1
        
print(f"la letra {letra} aparece {contador} veces en la frase {frase}")
