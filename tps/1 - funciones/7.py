"""
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una fecha cualquiera 
expresada por tres enteros y calcule y devuelva otros tres enteros correspondientes el día siguiente 
al dado. Utilizando esta función sin modificaciones ni agregados, desarrollar programas que permitan:

a)Sumar N días a una fecha
b)Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""
def is_leap_year(year:int)->bool:
    
    if year % 2 == 0:
        #Es bisiesto

        if year % 100 == 0:
            #No es bisiesto

            if year % 400 == 0:
                #Es bisiesto
                return True

            return False
        
        return True

def get_days_per_month (year:int)->dict[int, int]:
    """
    Make a dictionary custom for one year with the month number for key and the days of that month in the value
    
    Args:
        year (int)

    Returns:
        dict[int, int]: {month, n_days}
    """

    days_per_month:dict[int, int] = {
        1: 31,
        2: 28, #29 en bisiesto
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # Config days_per_moth
    if is_leap_year(year):
        days_per_month[2] = 29

    return days_per_month

def next_day(day:int, month:int, year:int)->tuple[int, int, int]:
    """
    Return (day, month, year)
    """
    days_per_month = get_days_per_month(year)

    #day ok
    if days_per_month[month] >= day+1:
        return (day+1, month, year)
    
    #month ok
    if 12 >= month+1:
        return (1, month+1, year)
    
    return (1, 1, year+1)

# a sin terminar
def a(n_days:int, date:tuple[int, int, int])->tuple[int, int, int]:

    new_date = next_day(*date)

    for _ in range(n_days - 1):
        new_date = next_day(*date)

    return new_date

# b sin terminar
def b(smaller_date:tuple[int, int, int], bigger_date:tuple[int, int, int])->int:

    if smaller_date == bigger_date:
        return 0
    
    new_date = next_day(*smaller_date)

    days_apart = 1

    while new_date != bigger_date:
        
        new_date = next_day(*new_date)

        days_apart += 1

    return days_apart
    

print(next_day(day=30, month=3, year=1700))
