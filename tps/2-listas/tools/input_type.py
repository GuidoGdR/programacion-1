from typing import Type, Callable, Any, Union

def input_type(input_message="Ingrese un valor: ", input_type:Type=str, error_message="Valor incorrecto", validator:Callable[[Any], Union[tuple[Exception, None], tuple[None, Any]]]=lambda x:(None, x))->Any:
    while True:
        usr_input = input(input_message)
                
        if input_type == int or input_type == float:
            
            if not usr_input.isnumeric():
                print(error_message)
                continue
            
            usr_input = input_type(usr_input)
            (validation_error_message, usr_input) = validator(usr_input)
            
            if validation_error_message != None:
                print(validation_error_message)
                continue

            return usr_input

        if input_type == str:
            
            usr_input = input_type(usr_input)
            (validation_error_message, usr_input) = validator(usr_input)

            if validation_error_message != None:
                print(validation_error_message)
                continue

            return usr_input