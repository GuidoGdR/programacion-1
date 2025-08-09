"""
Desarrollar una función que reciba tres números enteros positivos correspondientes al 
día, mes, año de una fecha y verifique si corresponden a una fecha válida.
Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no.

Realizar también un programa para verificar el comportamiento de la función.
"""

def esBisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def diasMes(mes, anio):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2 and esBisiesto(anio):
        vDias=29
    else:
        vAuxi=mes-1
        vDias=dias_por_mes[vAuxi]
    
    return vDias

def validarFecha(vDia, vMes, vAnio):
    if vAnio <= 0:
        return False
    if 1 <= vMes <= 12:
        vCantDias=diasMes(vMes,vAnio)
        if 1 <= vDia <= vCantDias:
            return True
        else:
            return False
    else:
        return False

def main():
    vDia=int(input("Ingrese el dia: "))
    vMes=int(input("Ingrese el mes: "))
    vAnio=int(input("Ingrese el anio: "))
    
    if validarFecha(vDia, vMes, vAnio):
        print("La fecha es válida")
    else:
        print("La fecha no es válida")

main()