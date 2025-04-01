a = 1

while a == 1:
    valor = int(input('Ingrese un valor: '))  # Pedimos el número

    for i in range(1, valor + 1):
        contador = 0
        for n in range(1, i + 1):
            if i % n == 0:
                contador += 1  

        if contador == 2:  
            print(f'{i} es un número primo')
        else:
            print(f'{i} NO es un número primo')

    # Preguntar al usuario si quiere continuar
    a = int(input("¿Deseas continuar? (1 = Sí, otro número = No): "))
