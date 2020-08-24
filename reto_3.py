notas = []
n = 1
num_notas = 0

while True:
    try:
        while num_notas <= 0:
            num_notas = int(input(f'Ingrese la cantidad de notas que va a promediar: '))
            if num_notas <= 0:
                print('Recuerde que la cantidad de notas debe ser un numero entero positivo y mayor a 0.')
        break
    except ValueError as e:
        print("Asegurese de que este ingresando un numero entero.")
    except Exception as e:
        print(e)

while True:
    try:
        while n <= num_notas:
            nota = float(input(f'Ingrese la nota {n}: '))
            if nota >= 0 and nota <= 20:
                notas.append(nota)
                n = n + 1
            else:
                print("Nota no valida. Recuerde que la calificación es de 0 a 20.")
        break
    except ValueError as e:
        print("Asegurese de que la nota ingresada sea un numero.")
    except Exception as e:
        print(e)

print(f'Las notas ingresadas son {notas}.')

nota_min = min(notas)
nota_max = max(notas)
prom = round(sum(notas)/num_notas)

print(f'La nota máxima es: {nota_max}')
print(f'La nota mínima es: {nota_min}')
print(f'El promedio de las notas es {prom}')
