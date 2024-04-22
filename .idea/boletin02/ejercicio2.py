"""
Ejercicio2 – Funciones
Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del
otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo
del segundo.
"""
#Funcion
def EsMultiplo(num1,num2):
    multiplo=False
    if num1 % num2==0:
        multiplo=True
    return multiplo
#Fin funcion


num1=int(input("Dame el numero 1: "))
num2=int(input("Dame el numero 2: "))
multiplo=False
bandera=False
print("\nSIN FUNCION")
if num1 % num2==0:
    print("El numero 1 es multiplo del numero 2")
    bandera=True

if num2 % num1==0:
    print("El numero 2 es multiplo del numero 1")
    bandera=True
if bandera==False:
    print("Ninguno de los dos numeros es multiplo del otro")


#LLamada a la Funcion
print("\nDESDE FUNCION")
multiplo=EsMultiplo(num1,num2)
if multiplo:
    print("El numero 1 es multiplo del numero 2")
else:
    print("El numero 1 NO es multiplo del numero 2")







