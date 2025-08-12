""" 
Martina compró N frutas en total, entre manzanas y peras.
Las manzanas cuestan $200 cada una y las peras $150 cada una.
En total gastó una cierta cantidad de pesos.
Según la cantidad de frutas y el total de pesos que pagó determinar
Cuántas manzanas y cuántas peras compró
"""

from typing import Union

def brute_force(total_fruit:int, total_price:int)->list[int, int, Union[Exception, None]]:
    apples_price = 200
    pears_price = 150
    total_apples, total_pears = 0, 0
    
    if total_price % apples_price == 0 and total_fruit == total_price / apples_price:
        return [int(total_price/apples_price), 0, None]
    
    if total_price % pears_price == 0 and total_fruit == total_price / pears_price:
        return [0, int(total_price/pears_price), None]

    for i in range(1, total_fruit): 
        total_pears = i
        total_apples = total_fruit - i

        if (total_pears * pears_price + total_apples * apples_price == total_price) and (total_apples + total_pears == total_fruit):
            return [total_apples, total_pears, None]
        
    return [0, 0, ValueError("No se a encontrado una combinacion posible entre peras y manzanas para dicho total de frutas por ese precio")]

print(brute_force(3, 550))#result[0]=manzanas, result[1]=peras,  result[2]=error si no se pudo encontrar combinacion posible

def ecuations_solution(total_fruit:int, total_price:int)->list[int, int, Union[Exception, None]]:
    pass