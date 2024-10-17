#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
Precio=str(input("¿Cuanto cuesta el producto? con dos decimales "))
dinero = Precio.split(".")
print("Tienes " + dinero[0] + "€ y " + dinero[1] + "centimos")