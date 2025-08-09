"""
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes.
Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes 
(detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro 
la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. 

Realizar también un programa para verificar el comportamiento de la función.
"""
# 1 a 20        normal
# 21 a 30       20%
# 31 a 40       30%
# mas de 40     40%

from typing import Callable

TRIP_PRICE = 500
# discount[x][0] = trips
# discount[x][1] = discount
# trips <= discount[x][0] have discount[x][1] of discount
DISCOUNTS = ((20, 0.00), (30, 0.20), (40, 0.30), (None,0.40))

def calc_discount_2(trips:int)->int:
    TRIP_PRICE = 500
    
    if trips <= DISCOUNTS[0][0]:
        return (TRIP_PRICE*trips)*DISCOUNTS[0][1]
    if trips <= DISCOUNTS[1][0]:
        return (TRIP_PRICE*trips)*DISCOUNTS[1][1]
    if trips <= DISCOUNTS[2][0]:
        return (TRIP_PRICE*trips)*DISCOUNTS[2][1]
    
    return (TRIP_PRICE*trips)*DISCOUNTS[3][1]

def calc_discount(trips:int)->int:
    
    result = [
        TRIP_PRICE-TRIP_PRICE*DISCOUNTS[0][1] if i <= DISCOUNTS[0][0] else 
        TRIP_PRICE-TRIP_PRICE*DISCOUNTS[1][1] if i <= DISCOUNTS[1][0] else 
        TRIP_PRICE-TRIP_PRICE*DISCOUNTS[2][1] if i <= DISCOUNTS[2][0] else 
        TRIP_PRICE-TRIP_PRICE*DISCOUNTS[3][1]
        for i in range(trips)
    ]    

    return sum(result)

def test_types(func:Callable[[int], int])->int:
    if type(func(1)).__name__ == "int":
        return True
    
    return False
