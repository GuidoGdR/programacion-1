"""
Escribir funciones lambda para:

a) Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener
 multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de 
 multiplicar 2 * 3.

b) Informar si un número es triangular. Un número se define como triangular si puede expresarse como 
la suma de un grupo de números naturales consecutivos comenzando desde 1. Por ejemplo 10 es un número triangular 
porque se obtiene sumando 1+2+3+4.

Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven True o False. 
No se permite utilizar ayudas externas a las mismas.
"""


oblongo = lambda vNum: any(vNum == vAux * (vAux + 1) for vAux in range(1, vNum))
triangular = lambda vNum: any(vNum == (vAux*(vAux+1))//2  for vAux in range(1, vNum+1) ) # k=(k*(k+1))/2 (Definicion algebraica de numero triangular)

#Ejemplos

print(oblongo(6))  # True
print(triangular(15))  # True → 1+2+3+4+5
print(triangular(8))   # False