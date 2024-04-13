"""
Ejercicio 4
Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
"""

numero_1=int(input("Numero 1: "))
numero_2=int(input("Numero 2: "))
numero_3=int(input("Numero 3: "))
if(numero_1>numero_2 and numero_1>numero_3):
    print("El numero 1 es el mayor de todos")
elif(numero_2>numero_1 and numero_2>numero_3):
    print("El numero 2 es el mayor de todos")
else:
    print("El numero 3 es el mayor de todos")