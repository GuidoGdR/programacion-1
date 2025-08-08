"""
Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva 
como valor de retorno el número que resulte de concatenar ambos parámetros. Por ejemplo, 
si recibe 1234 y 567 debe devolver 1234567. 
No se permite utilizar facilidades de Python no vistas en clase.
"""
def count_digits_of_number(number:int)->int:
    if number < 0: number = number * -1

    if number <= 10: return 1

    count = 1

    while True:
        calc_result = 10*count
        
        if calc_result == number: return count

        if calc_result > number: return count - 1

        count += 1

def union_strings_sin_ser_strings_y_retornando_int(a:int, b:int)->int:
    return a * ( 10**count_digits_of_number(b) ) + b

print(union_strings_sin_ser_strings_y_retornando_int(1,2))