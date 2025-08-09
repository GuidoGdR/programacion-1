"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique 
al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, 
correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada 
denominación deben ser entregados como vuelto, de tal forma que se minimice la cantidad de billetes. 
Considerar que existen billetes de $5000, $1000, $500, $200, $100, $50 y $10. 

Emitir un mensaje de error si el dinero recibido fuera insuficiente o si el cambio no pudiera entregarse 
debido a falta de billetes con denominaciones adecuadas. 

Ejemplo: Si la compra es de $3170 y se abona con $5000, el vuelto debe contener 1 billete de $1000, 
1 billete de $500, 1 billete de $200, 1 billete de $100 y 3 billetes de $10.
"""
# billetes de $5000, $1000, $500, $200, $100, $50 y $10. 
from typing import Union

def calculate_change(total:float, pay:float)->tuple[Union[None, Exception], tuple[int], tuple[int]]:
    money_types = (5000, 1000, 500, 200, 100, 50, 10)
    money_types_len = money_types.__len__()
    
    if total > pay:
        return (ValueError("Error, el direno recibido es insuficiente."), money_types, (0) * money_types_len)
    
    if  pay % 10 != 0:
        return (ValueError("Error, no hay billetes de denominacion adecuada."), money_types, (0) * money_types_len)
    print(pay % 10 )

    results:list[int, int, int, int, int, int, int] = [0] * money_types_len

    pay = pay - total
    for money_type_index in range(money_types_len):
        money_type = money_types[money_type_index]

        if pay >= money_type:

            n_of_this = pay / money_type
            
            spare = n_of_this - int(n_of_this)

            results[money_type_index] = int(n_of_this)
            
            pay = int(spare * money_type)

            if pay == 0:
                break
    
    return ( None, money_types, (results[:]) )

def interface():
    while True:
            
        total = float(input("Importe a cobrar: "))
        pay = float(input("Monto pagado: "))
        
        [err, money_types, quantities] = calculate_change(total, pay)

        if err:
            print(f"{err.__str__()}")

        else:
            for i in range(money_types.__len__()):

                print(f"{quantities[i]}\tde\t{money_types[i]}")

        if input("-1 para salir, cualquier otra cosa para continuar") == "-1":
            break


interface()