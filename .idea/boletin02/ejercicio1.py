"""
Ejercicio 1 - Diccionarios
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones
de cada carácter en la cadena.
"""

cadena=input("Dame la cadena a leer: ")
diccionario={}
contador=0
for i in cadena:
    diccionario[i]=0
for i in cadena:
    diccionario[i]=diccionario[i]+1

print(diccionario)