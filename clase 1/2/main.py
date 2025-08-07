from tools.count_ones import count_ones

def main():
    # (n es el numero que le determina la abuela)
    n = 'n'
    #input
    while not(n.isnumeric()):
        n = input('N = ')
    n = int(n)
    
    #get results
    #result[0]=x, result[1]=y, result[2]=ones_counted
    result:tuple[int, int, int] = (0, )*3
    y=1

    limit= n//2
    #(si no es par cortamos antes)
    if n/2 == n//2:
        limit -= 1
    for x in range(n-1, limit , -1):

        ones_counted = count_ones(x) + count_ones(y)
        if ones_counted > result[2]:
            result = (x, y, ones_counted)
        
        y += 1
    
    #show results
    print(f'X={result[0]} Y={result[1]} Ganancia={result[2]}')

if __name__ == '__main__':
    main()