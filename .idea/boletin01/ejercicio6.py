"""
Ejercicio 6
Realizar un programa que comprueba si una cadena leída por teclado comienza por una
subcadena introducida por teclado.
"""

cadena=input("Introduce la cadena: ")
subcadena=input("Introduce la subcadena: ")
num_caracteres= len(subcadena)

if(subcadena==cadena[0:num_caracteres]):
    print("La cadena introducida empieza por la subcadena")
else:
    print("La cadena introducida NO empieza por la subcadena")
