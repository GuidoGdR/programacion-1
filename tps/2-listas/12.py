"""
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, 
se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de 
carga. Se solicita:

a)Informar para cada socio, cuántas veces ingresó al club. Cada socio debe aparecer una sola vez en el informe.

b)Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.
"""

from typing import Union

from tools.input_type import input_type

def membership_number_validator(user_input:str)->Union[tuple[Exception, None], tuple[None, str]]:

    if not user_input.isnumeric():
        return (ValueError("El numero de socio no puede tener letras ni simbolos"), None)
    
    if user_input.__len__() != 5:
        return (ValueError("El numero de socio debe tener 5 digitos"), None)
    
    return (None, user_input)

def main_interface_validator(user_input:str)->Union[tuple[Exception, None], tuple[None, str]]:
    
    if user_input == "0" or user_input == "1" or user_input == "2":
        return (None, user_input)
    
    return main_interface_validator(user_input)

def main():
    income_list:list[str] = []
    
    while True:
        usr_input:str = input_type(
            input_message='0 para finalizar \n1 para informe \n2 para eliminar socio \nNumero de socio:', 
            input_type=str, validator=main_interface_validator)
        
        if usr_input == "1":

            """
            #opcion facil
            for i in set(income_list):

                print(f"numero de socio: {i}")
                print(f"numero de entradas: {income_list.count(i)}")
                print()
            """ 
            
            members = []
            count = []
            for member_number in income_list:

                if member_number in members:
                    count[members.index(member_number)] += 1
                    continue
                
                members.append(member_number)
                count.append(1)
                

            for member_index in range(members):
                print(f"numero de socio: {members[member_index]}")
                print(f"numero de entradas: {count[member_index]}")
                print()

        if usr_input == "2":

            print(income_list)
            
            usr_input:str = input_type(
                input_message='Numero de socio a eliminar:', 
                input_type=str, validator=membership_number_validator)
            
            member_count = income_list.count(usr_input)
            
            if not member_count:
                print("No existen registros de tal miembro")
                continue

            print(f"El miembro se encontro en {member_count} entradas")
            
            for _ in range(member_count):
                income_list.remove(usr_input)
            
            print(income_list)
            

        
        if usr_input == "0":
            break

        income_list.append(usr_input)
    


        

print("001a".isnumeric())