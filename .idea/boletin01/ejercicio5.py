"""
Ejercicio 5
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
media de todos los números introducidos.

"""


numero=-1
contador=0
suma=0
media=0

while(numero!=0):
    numero=int(input("Dame numero, 0 para terminar: "))
    if(numero!=0):
        contador+=1
        suma+=numero

print("\n\n")
print("La suma de todos los numeros es:",suma)
print("Has introducido:",contador," numeros")
print("La media de todos los numeros es:",suma/contador)

