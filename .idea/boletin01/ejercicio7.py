"""
Ejercicio 7
Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
"""

cadena=input("Dame la cadena a comprobar: ")
contador=0
char=" "

for i in cadena:
    if(i==" " and char!=" "):
        contador=contador+1
    char=i
print ("La frase tiene ",contador+1," palabras")


