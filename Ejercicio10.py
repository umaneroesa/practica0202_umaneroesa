#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
cesta = input('Dime los productos de la cesta (separados por comas) ')
c=cesta.split(",")
n=len(c)
x=0
while n > 0:
    print(c[x])
    x=x+1
    n=n-1