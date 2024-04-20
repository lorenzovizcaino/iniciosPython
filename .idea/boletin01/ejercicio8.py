"""
Ejercicio8
Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
(comprendidas entre 0 y 10). A continuación, debe mostrar: todas las notas, la nota media,
la nota más alta que ha sacado y la menor.
"""

notas=[0.0]*5
nota=-1
contador=0


for i in notas:
    while nota<0 or nota>10:
        nota=float(input("Nota "+str(contador+1)+": "))
        if(nota<0 or nota>10):
            print("nota incorrecta (rango entre 0/10)")
    notas[contador]=nota
    contador+=1
    nota=-1


notamedia=0
sumanotas=0
notamenor=11
notamayor=0
contador=0
print ("Las notas del alumno son:")
for i in notas:
    contador+=1
    sumanotas+=i
    print("nota "+str(contador)+": "+str(i))
    if i>notamayor:
        notamayor=i
    if i<notamenor:
        notamenor=i

print("La nota media del alumno es: "+str(sumanotas/5))
print("La nota mayor del alumno es: "+str(notamayor))
print("La nota menor del alumno es: "+str(notamenor))



