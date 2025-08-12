def verificar_nueva_nota(nota_a_validar:str)->bool:
    try:
        nota = int(nota_a_validar)
        
        assert nota > 10 and nota < 0, 'Nota fuera de rango.'

        return True

    except Exception:
        print('Nota incorrecta, no es un entero.')
        return False

