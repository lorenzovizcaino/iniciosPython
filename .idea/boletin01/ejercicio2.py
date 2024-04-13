"""
Ejercicio 2
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales
"""

nombre_persona=input("Nombre de la persona: ")
apellido_1=input("Apellido 1 de la persona: ")
apellido_2=input("Apellido 2 de la persona: ")
iniciales=nombre_persona[0]+" "+apellido_1[0]+" "+apellido_2[0]
print("las iniciales del nombre introducido son: "+ iniciales)