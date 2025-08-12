def custom_bin(number:int)->str:
    if number == 0:
        return '0'

    result = []
    
    quotient = number
    while True:

        result.insert(0, str(quotient%2))
        quotient = quotient // 2

        if quotient == 0:
            break
    
    return ''.join(result)
