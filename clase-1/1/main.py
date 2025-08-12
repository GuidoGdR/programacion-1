from validators.verificar_nueva_nota import verificar_nueva_nota


lambda num1,num2: sum(num1, num2) / 2

def main():
    notas_alumnos = []

    while True:
        print(notas_alumnos)
        
        nueva_nota = input('Nota 1 o -1 para salir: ')

        if nueva_nota == '-1':
            break

        alumno = []
        if verificar_nueva_nota(nueva_nota):
            alumno.append(int(nueva_nota))

        else:
            continue

        nota_n = 2
        
        while True:
            if nota_n == 4:
                notas_alumnos.append(alumno)
                break
            
            nueva_nota = input(f'agregar nota {nota_n}: ')
            
            if verificar_nueva_nota(nueva_nota):
                alumno.append(int(nueva_nota))
                nota_n += 1
            
