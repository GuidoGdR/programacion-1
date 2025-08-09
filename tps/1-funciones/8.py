"""
La siguiente función permite averiguar el día de la semana 
para una fecha determinada. La fecha se suministra en forma 
de tres parámetros enteros y la función devuelve 0 para domingo, 
1 para lunes, 2 para martes, etc. Escribir un programa para 
imprimir por pantalla el calendario de un mes completo, 
correspondiente a un mes y año cualquiera basándose en la 
función suministrada. Considerar que la semana comienza en 
domingo.
"""

def diadelasemana(dia:int, mes:int, año:int)->int:

    if mes < 3: 
        mes = mes + 10 
        año = año - 1 
    else: 
        mes = mes - 2 
    
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7 
    
    if diasem < 0: 
        diasem = diasem + 7 
    
    return diasem

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

def imprimirCalendario(mes, anio):
    # Encabezado
    print("Do Lu Ma Mi Ju Vi Sa")
    
    # Día de la semana del primer día del mes
    inicio = diadelasemana(1, mes, anio)
    
    # Espacios antes del primer día
    print("   " * inicio, end="") #Uso end="" para cambiar el salto default del print y reemplazarlo por ""
    
    # Días del mes
    for dia in range(1, diasMes(mes, anio) + 1):
        print(f"{dia:2}", end=" ") #Uso :2 para aumentar el ancho del numero a 2
        if (inicio + dia) % 7 == 0:  # Salto de línea cada sábado
            print()
    print()
    

# Ejemplo de uso
mes = int(input("Ingrese mes (1-12): "))
anio = int(input("Ingrese año: "))
imprimirCalendario(mes, anio)