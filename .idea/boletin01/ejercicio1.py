
"""
Ejercicio 1
Un alumno desea saber cual será su calificación final en la materia de Matemáticas. Dicha
calificación se compone de los siguientes porcentajes:
 55% del promedio de sus tres calificaciones parciales.
 30% de la calificación del examen final.
 15% de la calificación de un trabajo final.
"""

notaparcial1=float(input("Nota parcial 1: "))
notaparcial2=float(input("Nota parcial 2: "))
notaparcial3=float(input("Nota parcial 3: "))

notaexamenfinal=float(input("Nota examen final: "))

notatrabajo=float(input("Nota trabajo: "))

notaparcial=(notaparcial1+notaparcial2+notaparcial3)/3
nota_parcial_porcentaje=(notaparcial*55)/100
nota_examen_final_porcentaje=(notaexamenfinal*30)/100
notatrabajo_porcentaje=(notatrabajo*15)/100
nota_final=nota_parcial_porcentaje+nota_examen_final_porcentaje+notatrabajo_porcentaje
print("La nota final de matematicas es: ", nota_final)



