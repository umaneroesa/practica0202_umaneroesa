#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
fecha = input("¿Cual es la fecha de tu nacimiento? en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])
fecha = input("¿Cual es la fecha de tu nacimiento?")
n=fecha.split("/")
dia=n[0]
mes=n[1]
año=n[2]
print("Cumples el dia " + dia + " del mes " + mes + " y del año " + año)