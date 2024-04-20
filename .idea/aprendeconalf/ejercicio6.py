"""
Escribir un programa que lea un entero positivo,
n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta
n. La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:
 suma=n(n+1)/2
"""

numero=int(input("Dame el numero: "))
suma=(numero*(numero+1))/2
print("La suma es igual a: "+str(suma))

