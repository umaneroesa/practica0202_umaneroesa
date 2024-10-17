#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Escribeme una frase ")
n = len(frase)
print(frase[-1:-n-1:-1])