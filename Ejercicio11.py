#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input("Introduce el nombre del producto ")
precio = float(input("Introduce el precio unitario "))
unidades = int(input("Introduce el numero de unidades "))
total = precio*unidades 
print("el producto {} vale {:9.2f}€ y quiero {:3d} unidades, el total es {:11.2f}€".format(producto,precio,unidades, total))