"""
Desarrollar una función que reciba tres números enteros positivos y devuelva el mayor de los tres,
sólo si éste es único (es decir el mayor estricto).
Devolver -1 en caso de no haber ninguno.
No utilizar operadores lógicos (and, or, not).

Desarrollar también un programa para ingresar los tres valores, 
invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
"""
def funMayorTres(num1, num2, num3):
    vMayor=0
    
    if num1>num2:
        if num1>num3:
            vMayor = num1
        else:
            if num1==num3:
                vMayor=-1
            else:
                vMayor = num3
    elif num2>num3:
        if num2==num1:
            vMayor=-1
        else:
            vMayor=num2
    else:
        if num3==num2:
            vMayor=-1
        else:
            vMayor=num3
    return vMayor

def funMostrarMaximo():
    num1=int(input("Ingrese el primer numero: "))
    num2=int(input("Ingrese el segundo numero: "))
    num3=int(input("Ingrese el tercer numero: "))
    vMax=funMayorTres(num1, num2, num3)
    if vMax != -1:
        print("El Mayor ingresado es el numero:",vMax)
    else:
        print("No existe un mayor absoluto entre las opciones ingresadas")
    
def main():
    funMostrarMaximo()

main()