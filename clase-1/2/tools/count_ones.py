from tools.custom_bin import custom_bin

def count_ones(number:int)->int:
    
    bin_str = custom_bin(number)
    
    one_count = 0
    for i in bin_str:
        if i == '1':
            one_count += 1

    return one_count

def count_ones2(number:int)->int:
    
    bin_str = custom_bin(number)

    return bin_str.count('1')