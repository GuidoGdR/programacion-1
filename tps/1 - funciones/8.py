"""
La siguiente función permite averiguar el día de la semana para una fecha determinada. La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para imprimir por pantalla el calendario de un mes completo, correspondiente a un mes y año cualquiera basándose en la función suministrada. Considerar que la semana comienza en domingo.
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