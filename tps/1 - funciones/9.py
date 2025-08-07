"""
Resolver el siguiente problema utilizando funciones: 


Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar 
los camiones de reparto. La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada 
(500 kilogramos). En un cajón caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. 
Si el peso de alguna naranja se encuentra fuera del rango indicado se la clasifica para procesar como jugo. 

Desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden 
llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el 
siguiente reparto. Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.


Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando 
que la ocupación del camión no debe ser inferior al 80%; en caso contrario el camión no serán despachado 
por su alto costo.
"""

"""
En el punto 9:

Las nanjas fuera del rango (200-300) no son transportadas no?
no son contabilizadas para llenar cajones que iran en los camiones de reparto no?

"""
from random import randint




def main():
    crate_capacity_g = 100*300

    single_truck_capacity_g = 500 * 1000

    single_truck_capacity_crates = crate_capacity_g / single_truck_capacity_g

    oranges_n = input("Naranjas cosechadas: ")
    
    # calculate crates info
    crates = 0
    crate_now = 0

    for_juice = 0
    for _ in range(oranges_n):

        orange_weight = randint(150, 350)

        if orange_weight < 200 or orange_weight > 300:
            for_juice += 1
            continue

        crate_now += 1

        if crate_now == 100:
            crate_now = 0
            crates += 1
    
    
    if crate_now:
        
        crates += 1


    # show info
    print(f"Se pueden llenar {crates} cajones")
    
    if crate_now:
        print(f"Con un cajon sin llenar completamente el cual cuenta con:")
        print(f"{crate_now}/100 naranjas")


    # calculate trucks info
    filled_trucks = crates / single_truck_capacity_crates

    unfilled_truck = filled_trucks - filled_trucks.__trunc__()
    
    surplus=0
    
    if unfilled_truck >= 0.8:
        filled_trucks += 1

    else:
        surplus = unfilled_truck * single_truck_capacity_crates


    # show info
    print(f"Se pueden llenar {filled_trucks} camiones")
    
    if unfilled_truck >= 0.8:
        print(f"Con un camion sin llenar competamente el cual se llena al: {unfilled_truck*100}%")
    else:
        print(f"Con un sobrante de {surplus} cajones de naranjas")



if __name__ == "__main__":
    main()